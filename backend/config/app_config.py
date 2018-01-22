class AppConfig:

    #Image configurations

    public_image_url = "http://localhost/"

    public_upload_folder = "/var/www/html/ex"

    max_image_length = 16 * 1024 * 1024


    #Database configurations

    database_host = "localhost"

    database_user = "postgres"

    database_password = ""

    database_port = 5432

    database_name = "image_search_engine"