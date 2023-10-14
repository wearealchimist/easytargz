import os
import gtk 

def browse_file(widget):
    dialog = gtk.FileChooserDialog("Select a tar.gz file",
                                    None,
                                    gtk.FILE_CHOOSER_ACTION_OPEN,
                                    (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                     gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    dialog.set_default_response(gtk.RESPONSE_OK)

    filter = gtk.FileFilter()
    filter.set_name("Archives tar.gz")
    filter.add_pattern("*.tar.gz")
    dialog.add_filter(filter)

    response = dialog.run()
    if response == gtk.RESPONSE_OK:
        filepath = dialog.get_filename()
        install_tar_gz(filepath)
    dialog.destroy()

    def install_tar_gz(filepath):
        os.system(f"tar -xzvf {filepath}")
        print(f"File {filepath} has been extracted with success")

    window = gtk.Window()
    window.set_title("Install tar.gz file")
    window.set_default_size(400, 100)
    window.connecte("destroy", gtk.main_quit)

    vbox = gtk.Vbox()

    file_button = gtk.Button("Select file to install")
    file_button.connect("clicked", browse_file)

    vbox.add(file_button)
    window.add(vbox)

    window.show_all()

    gtk.main()