from pypdf import PdfReader, PdfWriter
import asyncio

reader = PdfReader("encrypted-pdf.pdf")
writer = PdfWriter()

def split_list(inp_list):
    sublist_length = len(inp_list) // 3
    sublist1 = inp_list[:sublist_length]
    sublist2 = inp_list[sublist_length:2 * sublist_length]
    sublist3 = inp_list[2 * sublist_length:]

    return sublist1, sublist2, sublist3

with open('wordlist.txt', 'r') as f:
    pass_list = f.readlines()

pass_list = [pwd.strip().replace("\n", "") for pwd in pass_list]

result1, result2, result3 = split_list(pass_list)

async def cracker(result):
    print("Started instance")
    for pwd in result:
        try:
            if reader.is_encrypted:
                reader.decrypt(pwd)
            if not reader.is_encrypted:
                break
        except Exception as e:
            print(f"Error: {e}")

    for page in reader.pages:
        writer.add_page(page)

    with open("decrypted-pdf.pdf", "wb") as f:
        writer.write(f)

async def main():
    await asyncio.gather(cracker(result1), cracker(result2), cracker(result3))

asyncio.run(main())
