import pytest
from pathlib import Path
from bs4 import BeautifulSoup

from pybel.page import Page

data_dir = Path(__file__).parent / 'data'


@pytest.fixture
def page_contents_raw():
    """Return soup of page"""
    with open(data_dir / 'page.html', 'r') as f:
        raw_html = f.read()
    return raw_html


@pytest.fixture
def page_contents(page_contents_raw):
    """Return soup of page"""
    return BeautifulSoup(page_contents_raw, 'html.parser')


@pytest.fixture
def search_contents_raw():
    """Return soup search page"""
    with open(data_dir / 'search.html', 'r') as f:
        raw_html = f.read()
    return raw_html


@pytest.fixture
def search_contents(search_contents_raw):
    """Return soup search page"""
    return BeautifulSoup(search_contents_raw, 'html.parser')


@pytest.fixture
def valid_page():
    return Page(
        hexagon="0",
        wall=1,
        shelf=1,
        volume=1,
        page=1
    )


@pytest.fixture
def invalid_page():
    return Page(
        hexagon="0",
        wall=-1,
        shelf=666,
        volume=69,
        page=420
    )


@pytest.fixture
def test_page_from_search():
    return Page(
        hexagon="0yv9k7a3nt62ueq4sb6tagg3bihx7ej581usd6sbq0xxx6th4itikzrwkre0b3eg00zclwyu0q4b9zvf0zyd02w8nuxutiofjinqa6w03qxnrymqnyairddg7hz56jzreo7pbnp7lf8mdht17gnfu0ou8nrn4vocg2cmpqks9ho8ls7s13ixeimucnjt6nwgssq3h377j76m77dxvans54694zygosldi0g0efbnd4paglgb49sv6pri74gfweucx0w2cke48rcpzrm2deta751s859e6zq1r1x1g6afvcys6hgyyg5olxyrg7caxga56mr8zexynojw90k7hedy7f92olul88d3alj1if3qqfq4zqtycmkz7vgb54y7usuit6lqkk3pbyozcq0vhipgn4pozegk3w7m7wincqlnsfd7nj8c3ov5ujjb6tq3rmme9r0m27cti24mo899bk6mjlev27nmg6dtxzr8xadedjed2dwgopanhdzth4d0z29uuzah88x3uh1gdt35b998cv8f4mmobdwi8wna8mun588v2ac1de74fmy35evopme2yncxgeifwtghrm2jyzaat6h2cxhjzebevob86mk62wuu6118dbcldnit1lsqryxlm50k2qogx3pi7m0nhongnbau6qt8m2ezflkpbjqe5ua3rapz87jlafviski7j1h87e59y7eux7xti0k7or455mmu4wfo4vyu34oe0cehbmn1gsvo7kgbqyvmv0lrp2ele9e7mh6cwjm6xmaj2b0t4xmx2rwshdi5yjptzqd3gbmysqw9ukp3jpta0o5ebj1mwx2rmtkb9585kvd6hl62j8bnl68jgmaa31k89mrovmsg7obxko4c4zenhf07ht5gexfqej5ccd2tnoefj0k4kyex1o9rvjycfmrmtsxciyn013ob6m1xfoxftnwskwbicwg9gwxpop50lu4mciik61ioqiuvvhisyfjlkzrq082napfhlbzdvluejnlvr1w0hjmq4ywe0qeeg5he7phcw44zdbjh36lr0suw6lpggi80qpal541xxqmnmcuendh7al64qrj9kptls52zeifvfzf0aqha5h57ze1d3r3kzhe2xesdkas5dktpuyaytxc2ia0mjsl7vo2nvpv42phn2br6bf97mtauf5grpsn7jbudnh5o1k94szjpgi2qwxhzl09z2oz0loglu0ay2073i7v3mmsfzqwyu8h96uia2roh97zwtmxex8cnyor8jqsp6nbhl15s1kjj93bmkiaxyyv7ml70sy8xm04gp0tdhvo4mcadyc3eaf5tx5phw01pjiau3ix7oycuasiwetsfs57b1rabyl1xd21675kcfnw4osus82tkritknmck54fyug2r6uum4jr6jf2g637yfpq9o4wmxp2vqtsl2kyx9l909d5lpsw0uht9b9rflmb7puxelnjj4wo1xvfpuo5do9jh3c5b4cyyeikvtcnyj16rl5v166zlwi43kdlrsm6t9kvaaksazvagp1zoc65d5k99wllfgtt031a3d82bjon3ytjqdf1wi4ziubu100s7sdj6vkkji97srygvdif6d27x0grxefxjjb2lmx08eq6dkm9ew3u42yl79iiykpjlvn8cmbtsgbdhamj6neyf56ethk9jhvg0oa9s3r38jdztw5gr6o8lzzu0232pzrauhkzwqcnez3x3glqs0pamidyrd9arzvyc094yks63d2j8oa97muitp8sp74fcow3g37zd3vk8vjnpctj8y5r0m4pz31vq1amd9gz2tjbfgowkbi9xzhaagsa6awzhgq9trwrfim2po6a51ps3cuhar7oovsq6pglj11h121hehy6kwybv9wie0mmex0zq2vmb4kqjxqzmw1l28i16yde72yc318ombux05wwttk20rdf7o7p4frl4xj1kwxtculac87g524az9kesnyiemhmmebs9e2d312ksdvsqorqmn5j34sqezja15yv5j2b2wvu5w7p239et56smzr9q9xlzgupziqwo155471az7ey94gr0rt6zq2eopu5fy461h2yhmahnah7pg5rxd77uwzme0gv9rxiyue0c5te6vquk89phpcpplvbo3kyanxar4q1iws0sbcjhjy6mymy62qz8aw92uts1nkjagtwetng2fakp4ayr5s8u9hdd95gmpp9fg8mk94qbw9n5j9axpti8fwtbkol8z4fypb5pa71jascygl2s2s1v28yyy1d5qoequgnbjuwudn9jimdcpdncultm0pnrjkul3havr8voij8h5kpvi7ai51xmbbu0bgv7s8mrt9l3gn67tm2en8grcyf2t5y79tpypc4emy1djsv66tvga5cy8w98r9h8lsvc8q7zq2j29vle9a7gyirw3bva93q57lkh216l39zhvi923vvbwwufrrcnu5uffk9l0mg94hw0gdr88f2holq1r9rg0zlr7c7lakt9si9au28lv0q0crzkrscsbj0rdkcg1rtdsdikd3mo09r7nfc534zxxv9vb7nqyhcdjjc3xl39ug3crvt5ha03lx09uz6879ie5mpcaeszi0gbtn84d7ry2rcp3ccjdpz52dpzjgiwq48xh09chki4qknd0a2c8muqimxdwzaeahzk98saqowamau0c9njt6v8w2h6gljz5hi22xmam4emqpdarfc8q9kgy70id4zdkgmm2afpor4nupl8vk0iybiuku5akueabmkdve8647ipqsnad55rgw406ui8u8fplbtnauyr14aouzllxf0g5oxorvx73u3enjgs0cniyr4mf5rf64f0agjt7l4mxdkksurv9vg4zobh35mwzaz56fmb42ppm2gy30fmkbd10feogp4qsazcxpkvaykv6pdcjkfdkebj7v8l2rcccjpyikxlkdnjz27x65yc5vfy2k9h51ugun7h3z5b9nck609eikbatld6e2v5yoto1cp083j82wltfmrhfckhlwu1alj3t1s9exs1lfgjy8y7bibmdy6t54ake6ljpb741sey2fjdcuwe9v7zcvero0d02hvdsxblzq7tkuxuc14xq4uhax0mpcchixoqd88b67mbv0gof58438qntwumzriudghump213xvc2xzvhip14ns2n3tc4tj1nkdcl7qlj3n27q7fhy77pbdeoccbp0ahge",
        wall=1,
        shelf=1,
        volume=5,
        page=98
    )


@pytest.fixture
def mocker_page_response(mocker, page_contents_raw):
    """Mock a page response"""
    response_mocker = mocker.Mock()
    response_mocker.text = page_contents_raw

    return mocker.patch(
        'pybel.page.requests.post',
        return_value=response_mocker
    )


@pytest.fixture
def mocker_search_response(mocker, search_contents_raw):
    """Mock a search response"""
    response_mocker = mocker.Mock()
    response_mocker.text = search_contents_raw

    return mocker.patch(
        'pybel.page.requests.post',
        return_value=response_mocker
    )
