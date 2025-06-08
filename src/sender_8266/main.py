import espnow
from utime import sleep_ms

esp = espnow.ESPNow()
esp.active(True)

peer = b"\x8cO\x00\x16\x8b("
esp.add_peer(peer)


unique_id = "Card_001"
message = unique_id.encode("utf-8")


def main() -> None:
    while True:
        esp.send(peer, message)
        print("Sent message:", message)

        sleep_ms(500)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("exit...")
