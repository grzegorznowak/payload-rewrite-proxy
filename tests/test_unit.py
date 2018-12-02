import src.PReP as PReP


def test_template_tokenizer():

    template1 = "value=::token1::&value2=::token2::"
    template2 = "q=::param1::"

    dict1 = {
        "token1": "token_value1"
    }
    dict2 = {
        "token2": "token_value2"
    }
    dict3 = {
        "param1": "token_value3"
    }

    tokenized1 = PReP.tokenize(template1, dict1)
    tokenized2 = PReP.tokenize(template1, dict2)
    tokenized3 = PReP.tokenize(template2, dict3)

    assert tokenized1 == "value=token_value1&value2=::token2::"
    assert tokenized2 == "value=::token1::&value2=token_value2"
    assert tokenized3 == "q=token_value3"
