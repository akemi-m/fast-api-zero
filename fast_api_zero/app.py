from http import HTTPStatus

from fastapi import FastAPI

from fast_api_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


# System Under Test - SUT
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        **user.model_dump(),
        id=len(database) + 1,
    )

    database.append(user_with_id)

    return user_with_id


# @app.get('/html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
# def read_root_html():
#     return """
#     <html>
#         <head>
#             <h1> Olá, Mundo! </h1>
#         </head>
#     </html>"""
