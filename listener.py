import socket
import json
from ai_analyst import analyze_threat 

def start_ghost_sensor(port=9999):
    
    # This line prevents "Address already in use" errors
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"[*] Ghost Sensor listening on port {port}...")

    while True:
        try:
            client_socket, addr = server_socket.accept()
            print(f"[*] Connection from {addr[0]}")
            
            request = client_socket.recv(1024).decode('utf-8', errors='ignore')
            
            if request:
                print(f"[*] Payload received: {request.strip()}")
                print("[*]Sending to AI Analyst...")
                
                # --- This is where we call your AI ---
                analysis = analyze_threat(addr[0], request, port)
                
                if analysis.get("verdict") == "MALICIOUS":
                    print("\n" + "="*40)
                    print(f"ALERT! THREAT DETECTED")
                    print(f"Type: {analysis.get('attach_type')}")
                    print(f"Type:{analysis.get('confidence')}%")
                    print(f"Reason: {analysis.get('reasoning')}")
                    print("="*40 + "\n")
                else:
                    print(f"Log is safe!:{analysis.get('reasoning')}\n")
            
            client_socket.close()
        except Exception as e:
            print(f"Error handling connection: {e}")
            break

# --- THIS IS THE MISSING PART ---
if __name__ == "__main__":
    start_ghost_sensor()