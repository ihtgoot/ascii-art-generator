import sys


FILE_PATH = "./test.bmp"
WIDTH_OUT = 100

def get_char(val):
    if val>240:  return " "
    elif val>220: return "."
    elif val>200: return ","
    elif val>180: return ":"
    elif val>160: return "*"
    elif val>140: return "+"
    elif val>120: return "-"
    elif val>100: return "="
    elif val>80:  return "#"
    elif val>60:  return "%"
    elif val>40:  return "@"
    else:          return "$" 

def main():
    with open(FILE_PATH, 'rb') as f:
        f.seek(18)
        w_in = int.from_bytes(f.read(4), 'little')
        h_in = int.from_bytes(f.read(4), 'little')
        f.seek(10)
        offset = int.from_bytes(f.read(4), 'little')
        f.seek(offset)
        padding = (4-(w_in*3)%4)%4
        pixcels = []

        for y in range(h_in):
            row = []
            for c in range(w_in):
                b = int.from_bytes(f.read(1),'little')
                g = int.from_bytes(f.read(1),'little')
                r = int.from_bytes(f.read(1),'little')
                gray = int(0.299*r + 0.587*g + 0.114*b)
                row.append(gray)
            f.read(padding)
            pixcels.append(row)
    pixcels= pixcels[::-1]
    h_out = int(WIDTH_OUT*(h_in/w_in)*0.55)
    
    for y in range(h_out):
        line = ""
        for x in range(WIDTH_OUT):
            src_x = int(x * (w_in/WIDTH_OUT))
            src_y = int(y * (h_in/h_out))
            brightness = pixcels[src_y][src_x]
            line+=get_char(brightness)
        print(line)


if __name__ == "__main__":
    main()

