from logic.event_emitter import EventEmitter


def test_add_listener():
    emitter = EventEmitter()

    def listener(data):
        assert data == "test"

    emitter.add_listener("event", listener)
    assert listener in emitter.listeners["event"]


def test_remove_listener():
    emitter = EventEmitter()

    def listener(data):
        assert data == "test"

    emitter.add_listener("event", listener)
    emitter.remove_listener("event", listener)
    assert listener not in emitter.listeners["event"]


def test_fire_event():
    emitter = EventEmitter()
    result = []

    def listener1(data):
        result.append(data)

    def listener2(data):
        result.append(data * 2)

    emitter.add_listener("event", listener1)
    emitter.add_listener("event", listener2)
    emitter.fire_event("event", 5)

    assert result == [5, 10]


if __name__ == "__main__":
    test_add_listener()
    test_remove_listener()
    test_fire_event()