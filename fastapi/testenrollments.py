import asyncio
from httpx import AsyncClient, Limits
import time

REQUESTS = 100

async def request_api(client: AsyncClient, i: int):
    headers = {
    'X-DC-DEVKEY': 'BB2OJ3B4P5YGGK5TCH3FPAZLDTAOQAKZRWNYJDXN45JYPEXGGVT6JSHKWQYRAG7BN3PAABSDK2ISB77PD'
    }
    uri = 'https://localhost.digicert.com/services/v2/order/certificate/ssl_basic'
    null = None
    body = {
    "certificate": {
        "common_name": "cert-testing.net",
        "service_name": null,
        "dns_names": null,
        "csr": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIIEqTCCApECAQAwZDELMAkGA1UEBhMCVVMxHTAbBgNVBAMMFHd3dy5zb21lLXdl\r\nYnNpdGUuY29tMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5l\r\ndCBXaWRnaXRzIFB0eSBMdGQwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoIC\r\nAQDeAt0ghhs73MZLyUgY2MNZGjxJ9GvLKKN0pCEdIr6jtN1KAnWJfCrSEH3CTw3t\r\n3YEi+\/8IHi0+5PHMef5HvbJL23CEds\/7tUnrj2YIVn3gV5HgmBNaXlK47hOMTomS\r\nqHBDJJe3lXuDOP+TXyn59nTLTPa0GSel9agZaN9Y88VLLXG08uHGdgPgtyeQPuN6\r\ncgxAo5P40XY1u27fn65ueMBcy55Dp7aTZBpR15XnPmM9t67F6BDB2x1h6yKj0p0A\r\n4uV2Q1jBi6AnqjV9YbYhceMErC7Yst1ttHC6ufQeh\/eoonbxeW69dDV2BEI9\/c\/f\r\nwM6CVs1A12SHw6jSv34qW6l4d1WhO8F0XNG6lLA8VS9ze82rYLpEFyb6QLfuZXzr\r\nQ1VnrBjd+z2N1\/YRkWu6qwv\/JE6E7tr5OcTr+Ij5Zwf01BdUh6gA2XEWmpxy6JNn\r\nRB9NSL5oVgsnMVc985XmnIgwepZ4OOKJTDEFB\/86Wey21Dn5u25Wea3g95sto\/Hc\r\nTmB3YX4RG6R4bf7XxcPlWKqBLeZTvwZMeKQgzX7SCYLgrs6uaaWPXCX+2v5oipQc\r\n4cqGwW2\/EoHhVYVgSMJJNwM6oOlpbOciO8SaqvSPAWfMAvmm+NsyXhBkZKW0rt47\r\nOQQH7+F+aCzisfDjXvRglyC3Wugfinub\/LeZM7ZePIIBYwIDAQABoAAwDQYJKoZI\r\nhvcNAQELBQADggIBALrNjazMNjBji8Kz2hSSK7i2t5g2NiA\/BXRBH1ITEhzkWvH6\r\ndHnVkyGOeytSMlmYlxWcdLHb9g2pti+GevnMOqn94b5\/wN+WLoUtuUAOB+Ve6xa4\r\nIGWOtF50htuvCNIKa5Xe+qwHrxVKQZjIhn8Md8elCR7fH1uj\/biDEuipNgnWr2Hb\r\n\/V9HAyoGJB\/ORinw5rVX+p2c2ReWgisXoj0Rq97gC1Fj8q3080MqU\/X2e+OdByGL\r\nIbbjWkUwSupP9+CgAt3izVRTV5NhjW5Vx+YmgGUBX35marUe8WyUNFz2ehuHLXJm\r\n+KhcBr3\/HkrlR1AJpKY\/tHISrQvdic7L9T\/hebSxISDgeXL1e4ZA6lqlmzAgL8z0\r\nkNx9f5V9hv5h3ZW8nPAUe3ZwzSUsN66w4BCpzfpiPnuX6aiMEMpNuPsrNhyri0Vr\r\nND38TR7d6ewYZlblNFaWJab7lml52v20dmRhwntOURmzc3iytWY4CJINSZYk0lP7\r\nPVRo98irdWVsvjo+KK3RrFCFrRp8\/iUsmCKP4D21zBZqy+hK035fE3lzZXccfvJW\r\nWbC\/KlbRqubD3OK99hsyKxqbdtXqzE1p3nBFKZTV1Jy1cqTe3yKuqdWC7L5Tebq6\r\nFVVWfM3DZJywjlHD44DujWWg47Z2zUQV\/sQWmmVWgdN92vDdX59EyhwM\/4pk\r\n-----END CERTIFICATE REQUEST-----",
        "signature_hash": "sha256",
        "organization_units": [],
        "organization": {
            "id": "1745124"
        },
        "server_platform": {
            "id": "11"
        },
        "ca_cert_id": null,
        "profile_option": null,
        "cert_validity": {
            "years": "1"
        }
    },
    "renewal_of_order_id": null,
    "custom_expiration_date": null,
    "comments": "Form autofill.",
    "container": {
        "id": "677793"
    },
    "auto_renew": null,
    "auto_reissue": null,
    "custom_renewal_message": "",
    "user_id_assignments": null,
    "additional_emails": [],
    "csa_agreed_to": "true",
    "disable_ct": "0",
    "dcv_method": "email",
    "certificate_dcv_scope": "base_domain",
    "locale": "en",
    "organization": {
        "id": "1745124",
        "contacts": [
            {
                "contact_type": "organization_contact",
                "first_name": "CertCentral",
                "last_name": "Admin",
                "job_title": "CC Admin",
                "telephone": "111-111-1111",
                "email": "cc.admin@cert-testing.com",
                "dom_id": 1,
                "user_id": 3924692,
                "type": "existing_contact"
            }
        ]
    },
    "order_validity": {
        "years": 1
    },
    "payment_method": "balance"
    }

    print(f"===> {i}")
    t = await client.post(uri, headers=headers, json=body, timeout=30)
    

    return f"<=== {i} {t.json()['id']}"


async def main():
    async with AsyncClient(limits=Limits(max_connections=40)) as client:
        aws = [asyncio.create_task(request_api(client, i)) for i in range(REQUESTS)]
        t = time.time()
        print(t, 'start')
        for coro in asyncio.as_completed(aws):
            earliest_result = await coro
            print(earliest_result, time.ctime())
        print(time.time() - t)
   


if __name__ == "__main__":
    asyncio.run(main())
