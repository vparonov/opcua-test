from datetime import datetime
import sys
sys.path.insert(0, "..")

from opcua import Client

if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()

        root = client.get_root_node()

        flip = root.get_child(["Objects", "1:Flip"])
        flop = root.get_child(["Objects", "1:Flop"])

        print(datetime.now())
        for i in range(10000):
            val_flip = flip.get_value()
            val_flop = flop.get_value() 
            #print(f"Flip = {val_flip}, Flop = {val_flop}")

            flip.set_value(val_flop)
        
        print(datetime.now())
    
    finally:
        client.disconnect()
