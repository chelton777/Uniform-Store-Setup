import reflex as rx
import re


class ContactState(rx.State):
    form_data: dict[str, str] = {}
    form_errors: dict[str, str] = {}
    is_submitting: bool = False

    @rx.event
    def is_valid_email(self, email: str) -> bool:
        return (
            re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$", email)
            is not None
        )

    def _validate_form(self, form_data: dict) -> bool:
        self.form_errors = {}
        if not form_data.get("name", "").strip():
            self.form_errors["name"] = "O nome é obrigatório."
        if not form_data.get("email", "").strip():
            self.form_errors["email"] = "O email é obrigatório."
        elif not self.is_valid_email(form_data["email"]):
            self.form_errors["email"] = "Por favor, insira um email válido."
        if not form_data.get("message", "").strip():
            self.form_errors["message"] = "A mensagem não pode estar vazia."
        return not self.form_errors

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        if not self._validate_form(form_data):
            yield rx.toast.error("Por favor, corrija os erros no formulário.")
            return
        self.is_submitting = True
        yield
        import asyncio

        await asyncio.sleep(2)
        self.is_submitting = False
        yield rx.toast.success(
            "Mensagem enviada com sucesso! Entraremos em contato em breve."
        )
        self.form_data = {}