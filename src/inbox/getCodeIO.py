import httpx,asyncio
class GetCode:
    def __init__(self,email:str) -> None:
        self.email = email
        self.client = self.__client_build()
    def __client_build(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(http2=True,follow_redirects=True)
    async def get(self) -> str:
        try:
            response = await self.client.get(f'https://api.internal.temp-mail.io/api/v3/email/{self.email}/messages')
            print(response.json())
            subject = response.json()[2]['subject']
            # اذا حساب جديد وتريد تسجل بيه بقيه 1 
            #  اذا سجلت بيه وتريد تغير ايميل غير قيمت واحد الى 2 واذا مجاب كود ضل زيد لحد مايطبعلك كود 
            code = subject.split(" is your TikTok code")[0]
            return code
        except Exception as e:
            return str(e) 

    
print(asyncio.run(GetCode(input("Email: ")).get()))