# The dumbest version that works

def set(key, value):
    """Saves data at the end of the file."""
    with open("db.txt", "a") as f:
        f.write(f"{key},{value}\n")

def get(key):
    """Reads the file line by line to find the last value of the key."""
    result = None
    try:
        with open("db.txt", "r") as f:
            for line in f:
                k, v = line.strip().split(",", 1)
                if k == key:
                    result = v
    except FileNotFoundError:
        return None
    
    # If the last thing we found was a tombstone, it means it's deleted
    if result == "__DELETED__":
        return None
        
    return result

def delete(key):
    """Point 3: Deletes by simply saving a tombstone value."""
    set(key, "__DELETED__")


# --- TEST ---
if __name__ == "__main__":
    set("team", "Alejandro, Gabriel, Jorge")
    print(get("team"))
    
    delete("team")
    print(get("team"))