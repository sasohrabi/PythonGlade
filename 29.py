import gtk as Gtk
import os
import signal
from subprocess import Popen, PIPE

##import gobject
##from gi.repository import Gtk
##from gi.repository import Gdk
##from gi.repository import GObject
##from gi.repository import GObject as gobject


##import gi.repository.Gdk
from suds import store

sub = []

class Handler:
    def onDeleteWindow(self, *args):

        global sub
        Popen("TASKKILL /F /PID {pid} /T".format(pid=sub.pid))
        Gtk.main_quit(*args)
        return

    def button1_clicked_cb(self, button):
        global sub
        builder.get_object("entry1").set_text("ali")
        self.liststore = builder.get_object('liststore1')
        self.liststore.append(["Row 1", "Row 2", "Row 3"])
        self.liststore.append(["Row 4", "Row 5", "Row 6"])
        # builder.get_object("treeview1").set_model(self.liststore)

        self.liststore2 = builder.get_object('liststore2')
        self.liststore2.append([10, "Select an Item:"])
        self.liststore2.append([11, "Row 1"])
        self.liststore2.append([12, "Row 2"])
        self.liststore2.append([13, "Row 3"])
        self.liststore2.append([14, "Row 4"])
        self.liststore2.append([15, "Row 5"])
        #sub.terminate()


        return

    # self.combobox = builder.get_object("combobox1")

    def button2_clicked_cb(self, button):
        builder.get_object("entry1").set_text("")

        #os.kill(sub.pid, signal.SIGINT)
        #sub.terminate()
        return
        ##out, err = sub.communicate()
        ##errcode = sub.returncode
        ##return errcode, out, err



    ##sub= os.startfile("H:\saeed\SAEED PROJECT\Lazarus\SQLite_Laz\project1.exe")

    def on_entry2_key_press_event(self, widget, ev, data=None):
        if ev.keyval == 65293:  ##.SHIFT_MASK: #If Escape pressed, reset text
            widget.set_text("")
            builder.get_object("entry1").set_text("")
            builder.get_object("entry1").grab_focus()


        ##           ## builder.get_object("entry1").get_toplevel().child_focus(gtk.DIR_TAB_FORWARD)
        ##           if ev.state == Gtk.gdk.BUTTON_PRESS_MASK:
        ##            widget.set_text("")
        ##            builder.get_object("entry1").set_text("")
        ##            builder.get_object("entry1").grab_focus()
        ##

    def on_combobox1_changed(self, widget, data=None):
        self.index = widget.get_active()
        self.model = widget.get_model()
        print "ComboBox Active Text is=", self.model[self.index][1]
        print "ComboBox Active Index is=", self.index
        print("Selected:ROW ID={}".format(self.model[self.index][0]))

    def on_treeview1_cursor_changed(self, selection):
        selection = builder.get_object('treeview1').get_selection()
        model, iter = selection.get_selected()
        print "treeview Active Text is=", model[iter][2]

    def create_model(self):
        testdata = [(1, 'Mihai', 'Ion'), (2, 'John', 'Doe'), (3, 'Silvester', 'Rambo')]
        for item in testdata:
            store.append([item[0], item[1], item[2]])
        return store


''' for multiple selecttion
		model, paths = selection.get_selected_rows()
		
		# Get the TreeIter instance for each path
		for path in paths:
		iter = model.get_iter(path)
'''

builder = Gtk.Builder()
builder.add_from_file("frm1.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
