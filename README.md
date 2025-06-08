# F1-25_UDP_Py

Python Script for parsing F1 25 UDP Telemetry

## Dependency
This requires **Construct** to be installed. Run ```pip install construct```

## How to use
- ```import parse``` at the top of the code.
- ```parse.getPacket()``` will return a tuple (bytes, Struct).
- Struct is the parser for corresponding packet type, so call Struct.parse(bytes) to obtain the values.
- Acquire individual values ```Struct.parse(bytes).m_packetFormat``` The name of the members are identical to the specs as June 9, 2025. [Link](https://forums.ea.com/blog/f1-games-game-info-hub-en/ea-sports%E2%84%A2-f1%C2%AE25-udp-specification/12187347)
- The parser names are also identical to the struct names in the specs.

## Example
```Python
data, parser = parse.getPacket()
telemetry = parser.parse(data)
print(telemetry)
```

## Notes
- getPacket() is a blocking call with a timeout of 1/360 seconds.
- To call individual parsers instead use ```parse.Packet_structs.{parser_name}```
- Some packets doesn't work--trying parsing such packet may result in exception.
- It's bit messy for now.
