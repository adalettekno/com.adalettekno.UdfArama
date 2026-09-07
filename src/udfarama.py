#!/usr/bin/env python3
import os
import threading
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GLib


APP_ID = "com.adalettekno.UdfArama"
APP_NAME = "UDF Belge Arama"


class UdfSearchWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title=APP_NAME)
        self.set_default_size(980, 680)
        self.selected_folder = None
        self.searching = False

        root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        root.set_margin_top(18)
        root.set_margin_bottom(18)
        root.set_margin_start(18)
        root.set_margin_end(18)
        self.set_child(root)

        header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
        root.append(header)

        self.folder_label = Gtk.Label(label="Arama klasörü seçilmedi", xalign=0)
        self.folder_label.set_hexpand(True)
        from gi.repository import Pango
        self.folder_label.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        header.append(self.folder_label)

        choose_btn = Gtk.Button(label="Klasör Seç")
        choose_btn.connect("clicked", self.choose_folder)
        header.append(choose_btn)

        self.search_entry = Gtk.Entry()
        self.search_entry.set_placeholder_text("Aranacak kelime veya ifade")
        self.search_entry.set_hexpand(True)
        self.search_entry.connect("activate", self.start_search)
        root.append(self.search_entry)

        self.search_button = Gtk.Button(label="Ara")
        self.search_button.connect("clicked", self.start_search)
        root.append(self.search_button)

        self.status = Gtk.Label(label="Önce bir klasör seçin.", xalign=0)
        root.append(self.status)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_vexpand(True)
        root.append(scrolled)

        self.model = Gtk.StringList()
        self.list_view = Gtk.ListView.new(
            Gtk.SingleSelection.new(self.model),
            Gtk.SignalListItemFactory()
        )
        factory = self.list_view.get_factory()
        factory.connect("setup", self._setup_item)
        factory.connect("bind", self._bind_item)
        self.list_view.connect("activate", self.open_selected)
        scrolled.set_child(self.list_view)

        self.load_saved_folder()

    def _setup_item(self, factory, item):
        item.set_child(Gtk.Label(xalign=0))

    def _bind_item(self, factory, item):
        label = item.get_child()
        label.set_text(item.get_item().get_string())

    def show_error(self, message):
        dialog = Gtk.AlertDialog(message=message)
        dialog.show(self)

    def load_saved_folder(self):
        config_dir = Path(GLib.get_user_config_dir()) / APP_ID
        path_file = config_dir / "folder"
        try:
            path = path_file.read_text(encoding="utf-8").strip()
        except OSError:
            return
        if path and os.path.isdir(path):
            self.selected_folder = path
            self.folder_label.set_text(path)
            self.status.set_text("Kayıtlı klasör hazır. Arama yapabilirsiniz.")

    def save_folder(self, path):
        config_dir = Path(GLib.get_user_config_dir()) / APP_ID
        config_dir.mkdir(parents=True, exist_ok=True)
        (config_dir / "folder").write_text(path + "\n", encoding="utf-8")

    def choose_folder(self, *_):
        dialog = Gtk.FileDialog(title="Arama yapılacak üst klasörü seçin")
        dialog.select_folder(self, None, self._folder_selected)

    def _folder_selected(self, dialog, result):
        try:
            file = dialog.select_folder_finish(result)
        except GLib.Error:
            return
        if file is None:
            return
        path = file.get_path()
        if not path:
            self.show_error("Seçilen konuma erişilebilir bir yerel yol alınamadı.")
            return
        self.selected_folder = path
        self.folder_label.set_text(path)
        self.save_folder(path)
        self.status.set_text("Klasör seçildi. Aramak istediğiniz ifadeyi girin.")

    def start_search(self, *_):
        if self.searching:
            return
        if not self.selected_folder or not os.path.isdir(self.selected_folder):
            self.show_error("Önce geçerli bir arama klasörü seçin.")
            return
        term = self.search_entry.get_text().strip()
        if not term:
            self.show_error("Aranacak ifade boş olamaz.")
            return

        self.searching = True
        self.search_button.set_sensitive(False)
        self.model.splice(0, self.model.get_n_items(), [])
        self.status.set_text("UDF dosyaları taranıyor…")
        threading.Thread(target=self._search_worker, args=(self.selected_folder, term), daemon=True).start()

    def _search_worker(self, folder, term):
        matches = []
        errors = 0
        lowered = term.casefold()

        for base, dirs, files in os.walk(folder, followlinks=False):
            dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(base, d))]
            for name in files:
                if not name.lower().endswith(".udf"):
                    continue
                path = os.path.join(base, name)
                try:
                    with zipfile.ZipFile(path) as archive:
                        try:
                            data = archive.read("content.xml")
                        except KeyError:
                            errors += 1
                            continue
                    text = data.decode("utf-8", errors="replace")
                    try:
                        root = ET.fromstring(text)
                        text = "\n".join(t for t in root.itertext() if t)
                    except ET.ParseError:
                        # Eski/bozuk XML yapılarında yine de düz metin aramasını dene.
                        pass
                    if lowered in text.casefold():
                        matches.append(path)
                except (OSError, zipfile.BadZipFile, RuntimeError):
                    errors += 1

        GLib.idle_add(self._search_finished, matches, errors)

    def _search_finished(self, matches, errors):
        for path in matches:
            self.model.append(path)
        self.status.set_text(
            f"Arama tamamlandı: {len(matches)} belge bulundu."
            + (f" ({errors} dosya okunamadı.)" if errors else "")
        )
        self.searching = False
        self.search_button.set_sensitive(True)
        return GLib.SOURCE_REMOVE

    def open_selected(self, list_view, position):
        item = self.model.get_string(position)
        if not item or not os.path.isfile(item):
            return
        uri = Gio.File.new_for_path(item).get_uri()
        try:
            Gio.AppInfo.launch_default_for_uri(uri, None)
        except GLib.Error as exc:
            self.show_error(f"Dosya varsayılan uygulamayla açılamadı:\n{exc}")


class UdfAramaApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID, flags=Gio.ApplicationFlags.DEFAULT_FLAGS)

    def do_activate(self):
        win = self.props.active_window
        if win is None:
            win = UdfSearchWindow(self)
        win.present()


app = UdfAramaApp()
app.run()
