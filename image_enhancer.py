"""
Image Enhancement for JEE Calculus Bot
Pre-processes images for better OCR accuracy by Gemini Vision
Same enhancement as chemistry bot: Contrast +30%, Sharpness +20%, Brightness +10%
"""

from PIL import Image, ImageEnhance
import os

class ImageEnhancer:
    def __init__(self):
        self.temp_dir = "temp_images"
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def enhance_image(self, image_path):
        """
        Enhance image for better OCR by Gemini Vision
        
        Args:
            image_path: Path to original image
            
        Returns:
            Path to enhanced image
        """
        try:
            # Open image
            img = Image.open(image_path)
            
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if too large (max 2048px on longest side)
            max_size = 2048
            if max(img.size) > max_size:
                ratio = max_size / max(img.size)
                new_size = tuple(int(dim * ratio) for dim in img.size)
                img = img.resize(new_size, Image.LANCZOS)
            
            # Enhancement 1: Increase Contrast by 30%
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(1.3)
            
            # Enhancement 2: Increase Sharpness by 20%
            sharpness_enhancer = ImageEnhance.Sharpness(img)
            img = sharpness_enhancer.enhance(1.2)
            
            # Enhancement 3: Increase Brightness by 10%
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(1.1)
            
            # Save enhanced image
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            enhanced_path = os.path.join(self.temp_dir, f"enhanced_{timestamp}.jpg")
            
            # Save with high quality (98)
            img.save(enhanced_path, 'JPEG', quality=98, optimize=True)
            
            print(f"✓ Image enhanced: {enhanced_path}")
            return enhanced_path
            
        except Exception as e:
            print(f"✗ Image enhancement error: {e}")
            # Return original path if enhancement fails
            return image_path
    
    def cleanup_temp_files(self):
        """Clean up temporary image files"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            os.makedirs(self.temp_dir, exist_ok=True)
