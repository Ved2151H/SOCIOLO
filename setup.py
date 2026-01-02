import os

def create_dir(path):
    os.makedirs(path, exist_ok=True)

def create_file(path):
    open(path, "a").close()

# ===============================
# ROOT STRUCTURE
# ===============================
create_dir("backend")
create_dir("mobile_app")
create_dir("docs")

# ===============================
# BACKEND (FastAPI)
# ===============================
create_dir("backend/app/core")
create_dir("backend/app/models")
create_dir("backend/app/schemas")
create_dir("backend/app/services")
create_dir("backend/app/api/endpoints")
create_dir("backend/app/utils")
create_dir("backend/tests")

create_file("backend/app/main.py")

create_file("backend/app/core/config.py")
create_file("backend/app/core/database.py")
create_file("backend/app/core/security.py")

create_file("backend/app/models/user.py")
create_file("backend/app/models/event.py")
create_file("backend/app/models/participation.py")
create_file("backend/app/models/safety_incident.py")

create_file("backend/app/schemas/user_schema.py")
create_file("backend/app/schemas/event_schema.py")
create_file("backend/app/schemas/panic_schema.py")

create_file("backend/app/services/user_service.py")
create_file("backend/app/services/event_service.py")
create_file("backend/app/services/panic_service.py")

create_file("backend/app/api/router.py")
create_file("backend/app/api/endpoints/auth.py")
create_file("backend/app/api/endpoints/events.py")
create_file("backend/app/api/endpoints/panic.py")

create_file("backend/app/utils/digipin.py")
create_file("backend/app/utils/geo.py")

create_file("backend/requirements.txt")
create_file("backend/.env")

# ===============================
# FLUTTER ANDROID APP
# ===============================
create_dir("mobile_app/lib/config")
create_dir("mobile_app/lib/models")
create_dir("mobile_app/lib/services")
create_dir("mobile_app/lib/screens")
create_dir("mobile_app/lib/widgets")
create_dir("mobile_app/lib/utils")
create_dir("mobile_app/android")

create_file("mobile_app/lib/main.dart")

create_file("mobile_app/lib/config/constants.dart")
create_file("mobile_app/lib/config/env.dart")

create_file("mobile_app/lib/models/user.dart")
create_file("mobile_app/lib/models/event.dart")
create_file("mobile_app/lib/models/panic.dart")

create_file("mobile_app/lib/services/api_service.dart")
create_file("mobile_app/lib/services/auth_service.dart")
create_file("mobile_app/lib/services/location_service.dart")

create_file("mobile_app/lib/screens/login_screen.dart")
create_file("mobile_app/lib/screens/map_screen.dart")
create_file("mobile_app/lib/screens/create_event_screen.dart")
create_file("mobile_app/lib/screens/event_detail_screen.dart")
create_file("mobile_app/lib/screens/panic_screen.dart")

create_file("mobile_app/lib/widgets/event_card.dart")
create_file("mobile_app/lib/widgets/panic_button.dart")
create_file("mobile_app/lib/widgets/loading_widget.dart")

create_file("mobile_app/lib/utils/permissions.dart")
create_file("mobile_app/lib/utils/emergency_actions.dart")

create_file("mobile_app/pubspec.yaml")

# ===============================
# DOCUMENTATION
# ===============================
create_file("docs/api_contract.md")
create_file("docs/safety_policy.md")
create_file("docs/panic_flow.md")
create_file("docs/future_features.md")

create_file("README.md")

print("Project structure created successfully.")
