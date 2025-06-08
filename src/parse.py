import socket
from packets import Packet_structs
from length import *
import signal, sys

def _sigint_handler(_, _):
    print("Exiting...")
    sys.exit(0)

IP_ADDR = '127.0.0.1'
PORT = 20777
socket.setdefaulttimeout(1/360)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_ADDR, PORT))

def sort_packet(data):
    if len(data) == Motion:
        return Packet_structs.PacketMotionData
    elif len(data) == Session:
        return Packet_structs.PacketSessionData
    elif len(data) == LapData:
        return Packet_structs.PacketLapData
    elif len(data) == Event:
        return None
        #return Packet_structs.PacketEventData
    elif len(data) == Participants:
        return Packet_structs.PacketParticipantsData
    elif len(data) == CarSetups:
        return Packet_structs.PacketCarSetupData
    elif len(data) == CarTelemetry:
        return Packet_structs.PacketCarTelemetryData
    elif len(data) == CarStatus:
        return Packet_structs.PacketCarStatusData
    elif len(data) == FinalClassification:
        return Packet_structs.PacketFinalClassificationData
    elif len(data) == LobbyInfo:
        return Packet_structs.PacketLobbyInfoData
    elif len(data) == CarDamage:
        return Packet_structs.PacketCarDamageData
    elif len(data) == SessionHistory:
        return Packet_structs.PacketSessionHistoryData
    elif len(data) == TyreSets:
        return Packet_structs.PacketTyreSetsData
    elif len(data) == MotionEx:
        return Packet_structs.PacketMotionExData
    elif len(data) == TimeTrial:
        return Packet_structs.PacketTimeTrialData
    elif len(data) == LapPositions:
        return Packet_structs.PacketLapPositionsData
    else:
        print(f"Unknown packet length: {len(data)}")
        print(data)
        pass

def getPacket():
    try:
        data, _ = sock.recvfrom(1500)
        parser = sort_packet(data)
        return data, parser
    
    except socket.timeout:
        return None, None
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, _sigint_handler)
    while True:
        try:
            data, addr = sock.recvfrom(1500)
            parser = sort_packet(data)

        except socket.timeout:
            continue
