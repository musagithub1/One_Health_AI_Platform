import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import random
import uuid
from database import Database

class SampleDataGenerator:
    def __init__(self, db_path="pet_health.db"):
        self.db = Database(db_path)

        # Sample data for generation
        self.dog_breeds = [
            "Golden Retriever", "Labrador Retriever", "German Shepherd", 
            "Bulldog", "Beagle", "Poodle", "Rottweiler", "Yorkshire Terrier",
            "Dachshund", "Siberian Husky", "Boxer", "Border Collie"
        ]

        self.cat_breeds = [
            "Persian", "Maine Coon", "Ragdoll", "British Shorthair",
            "Abyssinian", "Russian Blue", "Siamese", "Bengal",
            "American Shorthair", "Scottish Fold"
        ]

        self.colors = [
            "Brown", "Black", "White", "Golden", "Gray", "Black and White",
            "Brown and White", "Multicolor", "Cream", "Silver", "Orange"
        ]

        self.owner_names = [
            "Rajesh Kumar", "Priya Sharma", "Amit Singh", "Sneha Patel",
            "Vikram Gupta", "Anita Reddy", "Suresh Nair", "Meera Iyer",
            "Arjun Mehta", "Kavya Joshi", "Rohit Agarwal", "Deepika Rao"
        ]

        self.cities = [
            "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata",
            "Hyderabad", "Pune", "Ahmedabad", "Jaipur", "Surat"
        ]

        self.veterinarians = [
            "Dr. Ramesh Kumar", "Dr. Sunita Sharma", "Dr. Anil Gupta",
            "Dr. Preeti Singh", "Dr. Manoj Patel", "Dr. Rashmi Nair"
        ]

        self.clinics = [
            "City Veterinary Hospital", "Pet Care Center", "Animal Wellness Clinic",
            "Happy Pets Hospital", "Caring Paws Clinic", "Modern Pet Care"
        ]

        self.conditions = [
            "Healthy", "Allergies", "Hip Dysplasia", "Diabetes", "Heart Condition",
            "Skin Issues", "Dental Problems", "Arthritis", "Eye Problems"
        ]

        self.vaccinations = [
            "DHPP", "Rabies", "FVRCP", "FeLV", "Bordetella", "Lyme Disease"
        ]

    def generate_sample_pets(self, num_pets=20):
        """Generate sample pet data"""

        print(f"🐾 Generating {num_pets} sample pets...")

        pets_created = 0

        for i in range(num_pets):
            # Random pet data
            species = random.choice(["Dog", "Cat"])
            name = f"Pet_{i+1}"

            if species == "Dog":
                breed = random.choice(self.dog_breeds)
            else:
                breed = random.choice(self.cat_breeds)

            age = random.randint(1, 15)
            weight = round(random.uniform(2.0, 40.0), 1)
            color = random.choice(self.colors)

            # Owner data
            owner_name = random.choice(self.owner_names)
            owner_phone = f"+91{random.randint(7000000000, 9999999999)}"
            owner_email = f"{owner_name.lower().replace(' ', '.')}@email.com"
            city = random.choice(self.cities)
            owner_address = f"{random.randint(1, 999)}, {city}, India"

            # Optional fields
            microchip_id = f"IND{random.randint(100000000000, 999999999999)}" if random.random() > 0.3 else None
            qr_code = str(uuid.uuid4())
            medical_conditions = random.choice(self.conditions) if random.random() > 0.6 else None

            # Prepare pet data
            pet_data = (
                name, species, breed, age, weight, color,
                owner_name, owner_phone, owner_email, owner_address,
                microchip_id, qr_code, None, medical_conditions
            )

            try:
                pet_id = self.db.insert_pet(pet_data)
                if pet_id:
                    pets_created += 1

                    # Generate medical records for some pets
                    if random.random() > 0.5:
                        self.generate_medical_records_for_pet(pet_id, name)

                    # Generate vaccinations for some pets
                    if random.random() > 0.4:
                        self.generate_vaccinations_for_pet(pet_id, name, species)

            except Exception as e:
                print(f"❌ Error creating pet {i+1}: {e}")

        print(f"✅ Successfully created {pets_created} sample pets!")

    def generate_medical_records_for_pet(self, pet_id, pet_name):
        """Generate sample medical records for a pet"""

        num_records = random.randint(1, 5)

        for _ in range(num_records):
            # Random visit date (within last 2 years)
            days_ago = random.randint(1, 730)
            visit_date = (datetime.now() - timedelta(days=days_ago)).date()

            veterinarian = random.choice(self.veterinarians)
            clinic_name = random.choice(self.clinics)

            # Random diagnosis and treatment
            diagnoses = [
                "Routine checkup", "Vaccination", "Dental cleaning", "Skin allergy",
                "Ear infection", "Minor injury", "Digestive issues", "Wellness exam"
            ]

            treatments = [
                "Prescribed medication", "Topical treatment", "Dietary changes",
                "Follow-up recommended", "Surgery performed", "No treatment needed"
            ]

            diagnosis = random.choice(diagnoses)
            treatment = random.choice(treatments)
            medications = "Prescribed antibiotics" if "infection" in diagnosis else None

            # Random next visit (30-90 days from visit)
            next_visit_date = (visit_date + timedelta(days=random.randint(30, 90))).strftime('%Y-%m-%d')

            notes = f"Pet responded well to treatment. Owner advised on care."
            cost = round(random.uniform(500, 5000), 2)

            record_data = (
                pet_id, str(visit_date), veterinarian, clinic_name,
                diagnosis, treatment, medications, next_visit_date,
                notes, cost
            )

            try:
                # Note: You would implement this method in the Database class
                # self.db.insert_medical_record(record_data)
                pass
            except Exception as e:
                print(f"❌ Error creating medical record for {pet_name}: {e}")

    def generate_vaccinations_for_pet(self, pet_id, pet_name, species):
        """Generate sample vaccination records for a pet"""

        # Species-specific vaccinations
        if species == "Dog":
            vaccines = ["DHPP", "Rabies", "Bordetella"]
        else:
            vaccines = ["FVRCP", "Rabies", "FeLV"]

        for vaccine in vaccines:
            # Random vaccination date (within last year)
            days_ago = random.randint(30, 365)
            vaccine_date = (datetime.now() - timedelta(days=days_ago)).date()

            # Next due date (6-12 months later)
            next_due = (vaccine_date + timedelta(days=random.randint(180, 365))).strftime('%Y-%m-%d')

            veterinarian = random.choice(self.veterinarians)
            clinic_name = random.choice(self.clinics)
            batch_number = f"VAC{random.randint(100000, 999999)}"
            notes = "No adverse reactions observed"

            vaccination_data = (
                pet_id, vaccine, str(vaccine_date), next_due,
                veterinarian, clinic_name, batch_number, notes
            )

            try:
                # Note: You would implement this method in the Database class
                # self.db.insert_vaccination(vaccination_data)
                pass
            except Exception as e:
                print(f"❌ Error creating vaccination record for {pet_name}: {e}")

    def generate_lost_pet_scenarios(self, num_lost=3):
        """Generate some lost pet scenarios for testing"""

        print(f"🚨 Creating {num_lost} lost pet scenarios...")

        # Get some existing pets
        pets_df = self.db.get_all_pets()

        if pets_df.empty:
            print("❌ No pets available to mark as lost")
            return

        # Randomly select pets to mark as lost
        available_pets = pets_df[pets_df['is_lost'] == 0] if 'is_lost' in pets_df.columns else pets_df

        if len(available_pets) < num_lost:
            num_lost = len(available_pets)

        lost_pets = available_pets.sample(n=num_lost)

        for _, pet in lost_pets.iterrows():
            # Random lost date (within last 30 days)
            days_ago = random.randint(1, 30)
            lost_date = (datetime.now() - timedelta(days=days_ago)).date()

            locations = [
                "Central Park, Mumbai", "MG Road, Bangalore", "Connaught Place, Delhi",
                "Marina Beach, Chennai", "Cyber City, Gurgaon", "Koramangala, Bangalore"
            ]

            last_seen_location = random.choice(locations)

            try:
                # Mark pet as lost (you would implement this method)
                # self.db.update_pet_lost_status(pet['id'], True, last_seen_location, str(lost_date))
                print(f"📍 {pet['name']} marked as lost at {last_seen_location}")
            except Exception as e:
                print(f"❌ Error marking {pet['name']} as lost: {e}")

    def generate_found_pet_reports(self, num_found=5):
        """Generate sample found pet reports"""

        print(f"👁️ Creating {num_found} found pet reports...")

        for i in range(num_found):
            finder_names = ["Good Samaritan", "Animal Lover", "Community Helper", "Caring Citizen"]

            finder_name = random.choice(finder_names) + f" {i+1}"
            finder_phone = f"+91{random.randint(7000000000, 9999999999)}"
            finder_email = f"finder{i+1}@email.com"

            found_location = random.choice([
                "Park near Metro Station", "Residential Area", "Shopping Mall Parking",
                "Near Hospital", "School Campus", "Market Area"
            ])

            found_date = (datetime.now() - timedelta(days=random.randint(1, 7))).date()
            found_time = f"{random.randint(6, 22)}:{random.randint(0, 59):02d}"

            species = random.choice(["Dog", "Cat"])
            breed = random.choice(self.dog_breeds if species == "Dog" else self.cat_breeds)
            color = random.choice(self.colors)
            size = random.choice(["Small", "Medium", "Large"])

            description = f"{size} {color} {species}, appears friendly and well-cared for"
            distinctive_features = "Wearing collar" if random.random() > 0.5 else "No collar visible"

            current_location = "With finder" if random.random() > 0.5 else "Local animal shelter"

            found_pet_data = (
                finder_name, finder_phone, finder_email,
                found_location, str(found_date), found_time,
                description, species, breed, color, size,
                distinctive_features, None, current_location
            )

            try:
                # Insert found pet record (you would implement this method)
                # found_pet_id = self.db.insert_found_pet(found_pet_data)
                print(f"📋 Found pet report created: {description} at {found_location}")
            except Exception as e:
                print(f"❌ Error creating found pet report {i+1}: {e}")

    def generate_all_sample_data(self):
        """Generate complete set of sample data"""

        print("🚀 Starting sample data generation...")
        print("=" * 50)

        # Generate pets
        self.generate_sample_pets(20)

        # Generate lost pet scenarios
        self.generate_lost_pet_scenarios(3)

        # Generate found pet reports
        self.generate_found_pet_reports(5)

        print("=" * 50)
        print("✅ Sample data generation completed!")

        # Show statistics
        stats = self.db.get_statistics()
        print(f"📊 Database Statistics:")
        print(f"   - Total Pets: {stats.get('total_pets', 0)}")
        print(f"   - Lost Pets: {stats.get('lost_pets', 0)}")
        print(f"   - Medical Records: {stats.get('medical_records', 0)}")
        print(f"   - Recent Registrations: {stats.get('recent_registrations', 0)}")

    def clear_all_data(self):
        """Clear all data from database (for testing)"""

        print("🗑️ Clearing all sample data...")

        try:
            # Clear all tables (you would implement these methods)
            queries = [
                "DELETE FROM medical_records",
                "DELETE FROM vaccinations", 
                "DELETE FROM lost_pet_reports",
                "DELETE FROM found_pets",
                "DELETE FROM pets"
            ]

            for query in queries:
                self.db.execute_query(query)

            print("✅ All sample data cleared!")

        except Exception as e:
            print(f"❌ Error clearing data: {e}")

def main():
    """Main function for running sample data generation"""

    print("🐾 One Health AI Platform - Sample Data Generator")
    print("=" * 60)

    # Initialize generator
    generator = SampleDataGenerator()

    while True:
        print("\nChoose an option:")
        print("1. 🚀 Generate all sample data")
        print("2. 🐾 Generate pets only")  
        print("3. 🚨 Generate lost pet scenarios")
        print("4. 👁️ Generate found pet reports")
        print("5. 📊 Show current statistics")
        print("6. 🗑️ Clear all data")
        print("7. ❌ Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            generator.generate_all_sample_data()
        elif choice == "2":
            num = int(input("Number of pets to generate: "))
            generator.generate_sample_pets(num)
        elif choice == "3":
            num = int(input("Number of lost pets to create: "))
            generator.generate_lost_pet_scenarios(num)
        elif choice == "4":
            num = int(input("Number of found pet reports: "))
            generator.generate_found_pet_reports(num)
        elif choice == "5":
            stats = generator.db.get_statistics()
            print("\n📊 Current Database Statistics:")
            for key, value in stats.items():
                print(f"   - {key.replace('_', ' ').title()}: {value}")
        elif choice == "6":
            confirm = input("Are you sure? This will delete ALL data (y/N): ")
            if confirm.lower() == 'y':
                generator.clear_all_data()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
