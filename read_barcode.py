import cv2
from pyzbar.pyzbar import decode
  
def BarcodeReader(image):
     
    img = cv2.imread(image)
      
    detectedBarcodes = decode(img)
      
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
       
        for barcode in detectedBarcodes:            
            (x, y, w, h) = barcode.rect             
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
                print(barcode.data)
                print(barcode.type)
                 
    
 
if __name__ == "__main__":
    image="img1.png"
    BarcodeReader(image)