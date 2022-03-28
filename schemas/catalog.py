from pydantic import BaseModel, UUID4, Field


class CountryRequest(BaseModel):
    name: str = Field(title='Nombre', description='Nombre del país.', max_length=255, min_length=3, example='México')
    code_country: str = Field(title='Código', description='Código del país', max_length=255, example='52')
    coin_country: str = Field(title='Moneda', description='Moneda del país', max_length=255, example='mxn')
    symbol_country: str = Field(title='Símbolo', description='Símbolo del país', max_length=255, example='$')

    class Config:
        orm_mode = True


class CountryResponse(BaseModel):
    id: UUID4 = Field(title='ID', description='ID del objeto', example='d276ce8a-2dbe-4391-806a-8bf62456826f')
    name: str = Field(title='Nombre', description='Nombre del país.', max_length=255, min_length=3, example='México')
    code_country: str = Field(title='Código', description='Código del país', max_length=255, example='52')
    coin_country: str = Field(title='Moneda', description='Moneda del país', max_length=255, example='mxn')
    symbol_country: str = Field(title='Símbolo', description='Símbolo del país', max_length=255, example='$')

    class Config:
        orm_mode = True
