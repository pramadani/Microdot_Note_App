import network, time # type: ignore

SSID = "BOE-"
PASSWORD = ""

def network_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            print('connecting to network...')
            time.sleep(1)
    print('Connected! Network config:', sta_if.ifconfig())