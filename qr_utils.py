import qrcode
import io
import base64
from PIL import Image
import streamlit as st

class QRCodeGenerator:
    def __init__(self):
        self.base_url = "https://onehealth-ai.com/pet/"  # Base URL for pet profiles

    def generate_qr_code(self, pet_id, pet_name, owner_phone):
        """Generate QR code for a pet with contact information"""

        # Create QR code data - this could be a URL to the pet's profile or contact info
        qr_data = {
            'pet_id': pet_id,
            'name': pet_name,
            'contact': owner_phone,
            'url': f"{self.base_url}{pet_id}"
        }

        # Format as text for QR code
        qr_text = f"Pet: {pet_name}\nID: {pet_id}\nContact: {owner_phone}\nProfile: {qr_data['url']}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_text)
        qr.make(fit=True)

        # Create QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white")

        return qr_img, qr_text

    def create_pet_tag_design(self, pet_id, pet_name, owner_name, owner_phone, qr_img):
        """Create a complete pet tag design with QR code and info"""

        # Create a new image for the pet tag (300x400 pixels)
        tag_width, tag_height = 300, 400
        tag_img = Image.new('RGB', (tag_width, tag_height), 'white')

        # Resize QR code to fit the tag
        qr_size = 150
        qr_img_resized = qr_img.resize((qr_size, qr_size))

        # Calculate position to center QR code
        qr_x = (tag_width - qr_size) // 2
        qr_y = 50  # Leave space at top for text

        # Paste QR code onto tag
        tag_img.paste(qr_img_resized, (qr_x, qr_y))

        return tag_img

    def display_qr_code(self, pet_id, pet_name, owner_name, owner_phone):
        """Display QR code in Streamlit interface"""

        try:
            # Generate QR code
            qr_img, qr_text = self.generate_qr_code(pet_id, pet_name, owner_phone)

            # Create pet tag design
            tag_img = self.create_pet_tag_design(pet_id, pet_name, owner_name, owner_phone, qr_img)

            # Display in Streamlit
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 📱 QR Code")
                st.image(qr_img, caption=f"QR Code for {pet_name}", use_column_width=True)

                # Show QR code data
                st.markdown("**QR Code contains:**")
                st.text(qr_text)

            with col2:
                st.markdown("#### 🏷️ Pet Tag Design")
                st.image(tag_img, caption=f"Pet Tag for {pet_name}", use_column_width=True)

                # Instructions
                st.markdown("**Instructions:**")
                st.markdown("- Print this tag and attach to your pet's collar")
                st.markdown("- Anyone who finds your pet can scan the QR code")
                st.markdown("- The QR code contains your contact information")

            return qr_img, tag_img

        except Exception as e:
            st.error(f"Error generating QR code: {str(e)}")
            return None, None

    def generate_qr_for_lost_pet(self, pet_info, emergency_contacts):
        """Generate special QR code for lost pets with emergency info"""

        # Create emergency contact QR code
        emergency_text = f"LOST PET ALERT!\n"
        emergency_text += f"Name: {pet_info['name']}\n"
        emergency_text += f"Species: {pet_info['species']}\n"
        emergency_text += f"Breed: {pet_info.get('breed', 'Unknown')}\n"
        emergency_text += f"Color: {pet_info.get('color', 'Unknown')}\n"
        emergency_text += f"\nEMERGENCY CONTACTS:\n"

        for i, contact in enumerate(emergency_contacts, 1):
            emergency_text += f"{i}. {contact}\n"

        emergency_text += f"\nReward may be offered for safe return!"

        # Generate QR code with emergency styling
        qr = qrcode.QRCode(
            version=2,  # Larger version for more data
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=8,
            border=4,
        )
        qr.add_data(emergency_text)
        qr.make(fit=True)

        # Create QR code image with red styling for emergency
        emergency_qr = qr.make_image(fill_color="red", back_color="white")

        return emergency_qr, emergency_text

    def scan_qr_simulation(self, qr_text):
        """Simulate QR code scanning (for demo purposes)"""

        st.markdown("### 📱 QR Code Scanner Simulation")
        st.markdown("*This simulates what someone would see when scanning your pet's QR code*")

        # Display scanned information
        st.markdown("---")
        st.markdown("#### 🔍 Scanned Information:")

        # Parse the QR text and display nicely
        lines = qr_text.split('\n')
        for line in lines:
            if line.strip():
                st.markdown(f"**{line}**")

        # Action buttons that would appear in real scanner
        st.markdown("---")
        st.markdown("#### 📞 Quick Actions:")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.button("📞 Call Owner", help="Would dial the owner's number")

        with col2:
            st.button("📧 Send Email", help="Would open email to owner")

        with col3:
            st.button("📍 Report Location", help="Would report pet's current location")

        st.success("✅ Pet owner has been notified of your scan!")

    def convert_image_to_base64(self, img):
        """Convert PIL image to base64 string for storage"""

        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return img_str

    def create_downloadable_qr(self, pet_id, pet_name, owner_name, owner_phone):
        """Create downloadable QR code files"""

        try:
            # Generate QR code and tag
            qr_img, qr_text = self.generate_qr_code(pet_id, pet_name, owner_phone)
            tag_img = self.create_pet_tag_design(pet_id, pet_name, owner_name, owner_phone, qr_img)

            # Save images to bytes
            qr_bytes = io.BytesIO()
            tag_bytes = io.BytesIO()

            qr_img.save(qr_bytes, format='PNG')
            tag_img.save(tag_bytes, format='PNG')

            qr_bytes.seek(0)
            tag_bytes.seek(0)

            # Create download buttons
            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="📱 Download QR Code",
                    data=qr_bytes.getvalue(),
                    file_name=f"{pet_name}_qr_code.png",
                    mime="image/png"
                )

            with col2:
                st.download_button(
                    label="🏷️ Download Pet Tag",
                    data=tag_bytes.getvalue(),
                    file_name=f"{pet_name}_pet_tag.png",
                    mime="image/png"
                )

            st.info("💡 **Tip:** Print the pet tag on waterproof material for outdoor durability!")

        except Exception as e:
            st.error(f"Error creating downloadable QR codes: {str(e)}")

class QRCodeManager:
    """Manager class for QR code operations in the pet system"""

    def __init__(self, database):
        self.db = database
        self.generator = QRCodeGenerator()

    def create_pet_qr_system(self, pet_id):
        """Create complete QR code system for a pet"""

        # Get pet information from database
        pet_info = self.db.get_pet_by_id(pet_id)

        if pet_info.empty:
            st.error("Pet not found!")
            return

        pet = pet_info.iloc[0]

        st.markdown(f"### 🏷️ QR Code System for {pet['name']}")

        # Display QR code
        qr_img, tag_img = self.generator.display_qr_code(
            pet['id'], pet['name'], pet['owner_name'], pet['owner_phone']
        )

        if qr_img and tag_img:
            # Create downloadable versions
            self.generator.create_downloadable_qr(
                pet['id'], pet['name'], pet['owner_name'], pet['owner_phone']
            )

            # Show scanner simulation
            qr_text = f"Pet: {pet['name']}\nID: {pet['id']}\nContact: {pet['owner_phone']}\nProfile: {self.generator.base_url}{pet['id']}"

            if st.button("🔍 Simulate QR Scan", help="See what others see when they scan your pet's QR code"):
                self.generator.scan_qr_simulation(qr_text)

    def emergency_qr_system(self, pet_id, emergency_contacts):
        """Create emergency QR code system for lost pets"""

        pet_info = self.db.get_pet_by_id(pet_id)

        if pet_info.empty:
            st.error("Pet not found!")
            return

        pet = pet_info.iloc[0].to_dict()

        st.markdown("### 🚨 Emergency QR Code for Lost Pet")

        # Generate emergency QR code
        emergency_qr, emergency_text = self.generator.generate_qr_for_lost_pet(pet, emergency_contacts)

        # Display emergency QR
        col1, col2 = st.columns(2)

        with col1:
            st.image(emergency_qr, caption="Emergency QR Code", use_column_width=True)
            st.markdown("**Emergency QR Code - Red color indicates urgent pet recovery**")

        with col2:
            st.markdown("**Emergency Information:**")
            st.text(emergency_text)

        # Create downloadable emergency QR
        emergency_bytes = io.BytesIO()
        emergency_qr.save(emergency_bytes, format='PNG')
        emergency_bytes.seek(0)

        st.download_button(
            label="🚨 Download Emergency QR Code",
            data=emergency_bytes.getvalue(),
            file_name=f"{pet['name']}_emergency_qr.png",
            mime="image/png"
        )

        st.warning("🔄 **Share this emergency QR code on social media and with local communities to help find your pet!**")
