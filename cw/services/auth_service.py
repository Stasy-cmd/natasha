class AuthService:
    def register_new_user(self, data: dict):
        return self.user_service.create(data)


    def approve_refresh_token(self, refresh_token: str):
        data = jwt.decode(refresh_token, current_app.config["JWT_SECRET"],
                          algorithms=[current_app.config["JWT_ALGORITHM"]])
        email = data.get('email')

        user = self.user_service.get_by_email(email)

        if user is None:
            raise ItemNotFound

        return self.generate_token(email, user.password, is_refresh=True)

