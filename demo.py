from IPython import embed
import rtmidi_python as rtmidi


class Base(object):

    def __init__(self):
        self.events = {}

    def register_event(self, action_name, callback):
        if action_name not in self.events:
            self.events[action_name] = {}
        self.events[action_name] = callback

    def get_events(self):
        return self.events


class Slider(Base):

    def notify(self, level):
        if 'changed' in self.events:
            self.events['changed'](_level)


class Button(Base):
    def notify(self, level):

        if level == 127:
            if 'on' in self.events:
                self.events['on']()
        elif level == 0:
            if 'off' in self.events:
                self.events['off']()


class Knob(Base):

    def notify(self, level):
        if 'changed' in self.events:
            self.events['changed'](_level)


class Rew(Button):
    pass


class Play(Button):
    pass


class Loop(Button):
    pass


class Stop(Button):
    pass


class Rec(Button):
    pass


class Ff(Button):
    pass


class Kontrol:
    def __init__(self):
        self.items = {}
        self.events = {}
        self.items['rew'] = Rew()
        self.items['play'] = Play()
        self.items['ff'] = Ff()
        self.items['loop'] = Loop()
        self.items['stop'] = Stop()
        self.items['rec'] = Rec()
        for i in range(1, 10):
            self.items['knob%s' % i] = Knob()
            self.items['button%s_1' % i] = Button()
            self.items['button%s_2' % i] = Button()
            self.items['slider%s' % i] = Slider()

    def get_item(self, item_name):
        return self.items[item_name]

    def notify(self, item, level):
        if item in self.items:
            print "notify %s" % item
            self.items[item].notify(level)

    def get_events(self):
        return self.events

### Main ###


def rew_on_event():
    print 'rew_on_event'


def rew_off_event():
    print 'rew_off_event'


def play_on_event():
    print 'play_on_event'


def play_off_event():
    print 'play_off_event'


def ff_on_event():
    print 'ff_on_event'


def ff_off_event():
    print 'ff_off_event'


def loop_on_event():
    print 'loop_on_event'


def loop_off_event():
    print 'loop_off_event'


def stop_on_event():
    print 'stop_on_event'


def stop_off_event():
    print 'stop_off_event'


def rec_on_event():
    print 'rec_on_event'


def rec_off_event():
    print 'rec_off_event'


def knob_changed(_level):
    print "knob_changed_%s" % _level


def slider_changed(_level):
    print "slider_changed_%s" % _level


def button_on():
    print 'button_on'


def button_off():
    print 'button_off'

kontrol = Kontrol()

## rew button
rew_button = kontrol.get_item('rew')
rew_button.register_event('on', rew_on_event)
rew_button.register_event('off', rew_off_event)

# play button
play_button = kontrol.get_item('play')
play_button.register_event('on', play_on_event)
play_button.register_event('off', play_off_event)

## ff button
ff_button = kontrol.get_item('ff')
ff_button.register_event('on', ff_on_event)
ff_button.register_event('off', ff_off_event)

## loop button
loop_button = kontrol.get_item('loop')
loop_button.register_event('on', loop_on_event)
loop_button.register_event('off', loop_off_event)

## stop button
stop_button = kontrol.get_item('stop')
stop_button.register_event('on', stop_on_event)
stop_button.register_event('off', stop_off_event)

## rec button
rec_button = kontrol.get_item('rec')
rec_button.register_event('on', rec_on_event)
rec_button.register_event('off', rec_off_event)

## knob
knob1 = kontrol.get_item('knob1')
knob1.register_event('changed', knob_changed)

knob2 = kontrol.get_item('knob2')
knob2.register_event('changed', knob_changed)

knob3 = kontrol.get_item('knob3')
knob3.register_event('changed', knob_changed)

knob4 = kontrol.get_item('knob4')
knob4.register_event('changed', knob_changed)

knob5 = kontrol.get_item('knob5')
knob5.register_event('changed', knob_changed)

knob6 = kontrol.get_item('knob6')
knob6.register_event('changed', knob_changed)

knob7 = kontrol.get_item('knob7')
knob7.register_event('changed', knob_changed)

knob8 = kontrol.get_item('knob8')
knob8.register_event('changed', knob_changed)

knob9 = kontrol.get_item('knob9')
knob9.register_event('changed', knob_changed)

## slider
slider1 = kontrol.get_item('slider1')
slider1.register_event('changed', slider_changed)

slider2 = kontrol.get_item('slider2')
slider2.register_event('changed', slider_changed)

slider3 = kontrol.get_item('slider3')
slider3.register_event('changed', slider_changed)

slider4 = kontrol.get_item('slider4')
slider4.register_event('changed', slider_changed)

slider5 = kontrol.get_item('slider5')
slider5.register_event('changed', slider_changed)

slider6 = kontrol.get_item('slider6')
slider6.register_event('changed', slider_changed)

slider7 = kontrol.get_item('slider7')
slider7.register_event('changed', slider_changed)

slider8 = kontrol.get_item('slider8')
slider8.register_event('changed', slider_changed)

slider9 = kontrol.get_item('slider9')
slider9.register_event('changed', slider_changed)


for j in range(1, 9):
    for k in range(1, 3):
        button = kontrol.get_item('button%s_%s' % (j, k))
        button.register_event('on', button_on)
        button.register_event('off', button_off)


midi_in = rtmidi.MidiIn()
midi_in.open_port(0)

while True:
    message, delta_time = midi_in.get_message()
    if message:
        _id, _type, _level = message

        event_id = ''
        print _id, _type, _level
        if _type == 44:
            kontrol.notify('rec', _level)

        if _type == 45:
            kontrol.notify('play', _level)

        elif _type == 46:
            kontrol.notify('stop', _level)

        elif _type == 47:
            kontrol.notify('rew', _level)

        elif _type == 48:
            kontrol.notify('ff', _level)

        elif _type == 49:
            kontrol.notify('loop', _level)

        elif _type >= 2 and _type <= 6:
            event_id = "slider" + str(_type - 1)
            kontrol.notify(event_id, _level)

        elif _type >= 8 and _type <= 9:
            event_id = "slider" + str(_type - 2)
            print event_id
            kontrol.notify(event_id, _level)

        elif _type >= 12 and _type <= 13:
            event_id = "slider" + str(_type - 4)
            print event_id
            kontrol.notify(event_id, _level)

        elif _type >= 14 and _type <= 22:
            event_id = "knob" + str(_type - 13)
            kontrol.notify(event_id, _level)

        elif _type >= 23 and _type <= 31:
            event_id = "button%s_1" % str(_type - 22)
            kontrol.notify(event_id, _level)

        elif _type >= 33 and _type <= 41:
            event_id = "button%s_2" % str(_type - 32)
            kontrol.notify(event_id, _level)
