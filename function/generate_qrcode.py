import vobject
import qrcode

from utils.constant import *
from current_directory import dir_path


def generate_qrcode_main(personal):
    generate_vcf_resp = {}
    try:
        fullname = personal.pop(FULLNAME, "")
        profile_picture = personal.pop(PROFILE_PICTURE, "")
        date_of_birth = personal.pop(DATE_OF_BIRTH, "")
        gender = personal.pop(GENDER, "")
        job_title = personal.pop(JOB_TITLE, "")
        google_map = personal.pop(GOOGLE_MAP, "")
        company_name = personal.pop(COMPANY_NAME, "")
        about = personal.pop(ABOUT, "")
        website = personal.pop(WEBSITE, "")
        street = personal.pop(ADDRESS_LINE_1, "")
        extended_address = personal.pop(ADDRESS_LINE_2, "")
        city = personal.pop(CITY, "")
        map_location = personal.pop(MAP_LOCATION, "")
        country = personal.pop(COUNTRY, "")
        province = personal.pop(PROVINCE, "")
        district = personal.pop(DISTRICT, "")
        palika = personal.pop(PALIKA, "")
        city_village_name = personal.pop(CITY_VILLAGE_NAME, "")
        postal_code = personal.pop(POSTAL_CODE, "")
        postoffice_box = personal.pop(POSTOFFICE_BOX, "")
        phone_number = personal.pop(PHONE_NUMBER, "")
        email = personal.pop(EMAIL, "")

        address_parms = [
            country,
            province,
            district,
            palika,
            city_village_name,
            postal_code,
            postoffice_box,
        ]
        check_address_parms = all(v == "" for v in address_parms)

        v = vobject.vCard()

        if bool(fullname):
            v.add("FN").value = fullname

        if bool(date_of_birth):
            v.add("BDAY").value = date_of_birth

        if bool(gender):
            v.add("GENDER").value = gender

        if bool(map_location):
            # start = '@'
            # end = '/'
            # split_values = (map_location.split(start))[1].split(end)[0]
            # print(split_values.split(","))
            # print("google_map", map_location)
            v.add("GEO").value = map_location

        if bool(profile_picture):
            v.add("PHOTO").value = profile_picture

        if bool(job_title):
            v.add("TITLE").value = job_title

        if bool(company_name):
            v.add("ORG").value = [company_name]

        if bool(about):
            v.add("NOTE").value = about

        if bool(website):
            v.add("URL").value = website

        if not check_address_parms:
            v.add("ADR")
            v.adr.type_param = "HOME"
            v.adr.value = vobject.vcard.Address(
                street=street,
                city=city,
                region=province,
                code=postal_code,
                country=country,
                box=postoffice_box,
                extended=extended_address,
            )

        if bool(phone_number):
            for x in phone_number:
                v.add("TEL")
                v.tel.value = x["value"]
                v.tel.type_param = x["type"]

        if bool(email):
            for x in email:
                v.add("EMAIL")
                v.email.value = x["value"]
                v.email.type_param = x["type"]

        # with open("test.vcf", "w", newline="") as f:
        #     f.write(v.serialize())

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(v.serialize())
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        img.save(f"{dir_path}/qrcode.png")

    except Exception as e:
        msg = str(e)
        print("Error: " + msg)

    return generate_vcf_resp
