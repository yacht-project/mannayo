import random


taste = ['매운', '맵디맵운', '매옴한', '매움한', '매콤한', '매큼한', '맵짠', '신랄한', '달곰쌉쌀한', '달곰씁쓸한', '쌉싸래한', '쌉쌀한', '쓴', '쓰디쓴', '씁쓰레한', '새곰새곰한', '새금새금한', '새금한', '새척지근한', '새콤한', '새콤새콤한', '새콤달콤한', '새큼새큼한', '새큼한', '시금한', '시금시금한', '신', '시디신', '시지근한', '시큼시큼한', '감미로운', '달곰한', '달곰삼삼한', '달곰새금한', '달곰쌉쌀한', '달곰씁쓸한', '달금한', '달달한', '달보드레한', '들부드레한', '달짝지근한', '달착지근한', '달콤한', '달큼한', '들부드레한', '들쩍지근한', '들척지근한', '들큼한', '새큼달큼한', '구뜰한', '구수한', '담백한', '엇구뜰한', '엇구수한', '맹맹한', '모름한', '밍밍한', '바따라진', '배틀한', '비틀한', '삼삼한', '싱거운', '짐짐한', '칼칼한', '타분한', '텁지근한', '구스운', '쿠싱한', '슴슴한']

bread = ['감자 와플', '감자 팬케이크', '감자빵', '건빵', '공갈빵', '국화빵', '난', '납작빵', '단팥빵', '달걀빵', '담프누델', '댐퍼', '도넛', '도라야키', '도미빵', '도사', '라가나', '라바시', '라오빙', '라퓨타빵', '라호흐', '소말리아', '예멘', '레프세', '로티', '파키스탄', '롤빵', '루그브뢰드', '루말리 로티', '마늘빵', '미국', '마라케타', '마르코크', '막대빵', '만터우', '말루가', '맥주빵', '멜론빵', '몬트리올 스타일 베이글', '무교병', '미케타', '바게트', '바나나빵', '바노치카', '슬로바키아', '바르바리빵', '아프가니스탄', '바미', '바바', '바스테다', '바즐라마', '바크리', '파키스탄', '밤브랙', '배넉', '배라 브리스', '번', '베이글', '벨기에 와플', '보르딘스키', '볼라니', '부블리크', '불', '붕어빵', '브레첼', '브로아', '브루티보니', '브리오슈', '비스킷', '비엔나 빵', '빙', '사워도', '산가크', '생강빵', '소다빵', '소라빵', '소보로빵', '솔트라이징 브레드', '쇼티스 푸리', '스가베오', '스콘', '시르말', '쌀빵', '아나다마빵', '아레파', '아유야', '아이시 메라라', '아팜', '스리랑카', '아흐도브 크루차벨드', '에그 와플', '우유 토스트', '은저라', '에티오피아', '잉글리시 머핀', '제병', '이탈리아', '조니케이크', '차파티', '파키스탄', '체스니차', '초프', '독일', '추레키', '츠비바크', '치아바타', '칙피 브레드', '터키', '카놈 브앙', '캄보디아', '카레빵', '카아크', '카야 토스트', '말레이시아', '캐나디안 화이트', '코티지 로프', '코피아 페라레세', '콘브레드', '쿨차', '파키스탄', '퀵 브레드', '큐번 브레드', '크네케브뢰드', '크래커', '크럼펫', '크레이프', '크루통', '크리스마스 웨이퍼', '키스티비', '바시키르 공화국', '타랄리', '타이거 브레드', '타프툰', '탄두르빵', '텍사스 토스트', '토르티야', '토스트', '통밀빵', '툰브뢰드', '티케이크', '파네 디 알타무라', '파네 카라사우', '사르데냐', '파네 티치네세', '파네토네', '파라타', '파키스탄', '파로타', '파파덤', '판 둘세', '판데살', '판도로', '판브리오케', '판포카차', '팔', '팟브루드', '팡드미', '팬케이크', '페니 번', '페니아', '포카차', '푸가스', '푸란 폴리', '풀빵', '품퍼니켈', '프로야', '플라트브뢰드', '플라트카카', '피스톨레', '피아디나', '피자', '피타', '레바논', '할라', '호두과자', '호밀빵', '호박빵', '호빵', '황남빵', '흰빵', '힘바샤']

def get_random_bread():
    return random.choice(taste) + ' ' + random.choice(bread)
