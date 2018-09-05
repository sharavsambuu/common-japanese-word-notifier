#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	source : https://en.wiktionary.org/wiki/Appendix:1000_Japanese_basic_words
"""

import os
import random

dataset = """
嗚呼,ああ – Ah!, Oh!, Alas!
相,あい – together, mutually, fellow
相変わらず,あいかわらず – as ever, as usual, the same
愛想,あいそ – civility, courtesy, compliments, sociability, graces
相対,あいたい – confrontation, facing, between ourselves, no third party, tete-a-tete
間柄,あいだがら – relation(ship)
愛憎,あいにく – likes and dislikes
合間,あいま – interval
曖昧,あいまい – vague, ambiguous
敢えて,あえて – dare (to do), challenge (to do)
仰ぐ,あおぐ – to look up (to), to respect, to depend on, to ask for, to seek, to revere, to drink, to take
垢,あか – dirt, filth
亜科,あか – suborder, subfamily
銅,あかがね – copper
証,あかし – proof, evidence
赤字,あかじ – deficit, go in the red
明かす,あかす – to pass, spend, to reveal, to divulge
赤ちゃん,あかちゃん – baby, infant
明白,あからさま – obvious, overt, plainly, frankly
赤らむ,あからむ – to become red, to redden, to blush
明るい,あかるい – bright, cheerful
上がり,あがり – 1. slope, advance income, crop yield, ascent, rise, advance, death, spinning, completion, stop, finish, after
上がる,あがる – to enter, to go up, to rise, to climb up, to advance, to appreciate, to be promoted, to improve, to call on,
商人,あきうど – trader, shopkeeper, merchant
空間,あきま – vacancy, room for rent or lease
諦め,あきらめ – resignation, acceptance, consolation
呆れる,あきれる – to be amazed, to be shocked
悪,あく – evil, wickedness
灰,あく – puckery juice
,あくどい – 1. gaudy, showy, excessive, 2. vicious
悪日,あくび – unlucky day
明くる,あくる – next, following
憧れ,あこがれ – yearning, longing, aspiration
顎,あご – chin
麻,あさ – flax, linen, hemp
明後日,あさって – day after tomorrow
朝寝坊,あさねぼう – oversleeping, late riser
浅ましい,あさましい – wretched, miserable, shameful, mean, despicable, abject
字,あざ – section of village
欺く,あざむく – to deceive
鮮やか,あざやか – vivid, clear, brilliant
あざ笑う,あざわらう – to sneer at, to ridicule
味わい,あじわい – flavour, meaning, significance
東,あずま – east, Eastern Japan
焦る,あせる – to be in a hurry, to be impatient
彼処,あそこ – 1. (uk) there, over there, that place, 2. (X) (col) genitals
値,あたい – value, price, cost, worth, merit
値する,あたいする – to be worth, to deserve, to merit
私,あたし – I (fem)
当たり,あたり – hit, success, reaching the mark, per ..., vicinity, neighborhood
当たり前,あたりまえ – usual, common, ordinary, natural, reasonable, obvious
他人,あだびと – another person, unrelated person, outsider, stranger
彼方此方,あちこち – here and there
彼方,あちら – 1. there, yonder, that
彼方此方,あちらこちら – here and there
悪化,あっか – deterioration, growing worse, aggravation, degeneration, corruption
呆気ない,あっけない – not enough, too quick (short long etc.)
悪口,あっこう – abuse, insult, slander, evil speaking
,あっさり – easily, readily, quickly
圧迫,あっぱく – pressure, coercion, oppression
扱い,あつかい – treatment, service
集まる,あつまる – to gather, to collect, to assemble
誂える,あつらえる – to give an order, to place an order
圧力,あつりょく – stress, pressure
当て,あて – object, aim, end, hopes, expectations
宛,あて – addressed to
当て字,あてじ – phonetic-equivalent character, substitute character
当てはまる,あてはまる – to apply (a rule)
当てはめる,あてはめる – to apply, to adapt
宛てる,あてる – to address
跡継ぎ,あとつぎ – heir, successor
後回し,あとまわし – putting off, postponing
貴女,あなた – you, lady
彼の,あの – that over there
溢れる,あふれる – to flood, to overflow, to brim over
油絵,あぶらえ – oil painting
炙る,あぶる – to scorch
,あべこべ – contrary, opposite, inverse
甘える,あまえる – to behave like a spoiled child, to fawn on
甘口,あまくち – sweet flavour, mildness, flattery, stupidity
雨具,あまぐ – rain gear
天,あまつ – heavenly, imperial
網,あみ – net, network
天地,あめつち – heaven and earth, the universe, nature, top and bottom, realm, sphere, world
操る,あやつる – to manipulate, to operate, to pull strings
,あやふや – uncertain, vague, ambiguous
危ぶむ,あやぶむ – to fear, to have misgivings, to be doubtful, to mistrust
過ち,あやまち – fault, error, indiscretion
誤る,あやまる – to make a mistake
歩み,あゆみ – walking
歩む,あゆむ – to walk, to go on foot
,あら – oh, ah, saw-edged perch (Niphon spinosus)
予め,あらかじめ – beforehand, in advance, previously
荒らす,あらす – to lay waste, to devastate, to damage, to invade, to break into
粗筋,あらすじ – outline, summary
争い,あらそい – dispute, strife, quarrel, dissension, conflict, rivalry, contest
改まる,あらたまる – to be renewed
荒っぽい,あらっぽい – rough, rude
凡ゆる,あらゆる – all, every
,あられ – kind of cookie, cartoon character
現われ,あらわれ – embodiment, materialization
現われる,あらわれる – to appear, to come in sight, to become visible, to come out, to embody, to materialize, to express oneself
有難う,ありがとう – Thank you
有様,ありさま – state, condition, circumstances, the way things are or should be, truth
有りのまま,ありのまま – the truth, fact, as it is, frankly
或る,ある – a certain..., some...
或いは,あるいは – or, possibly
彼此,あれこれ – one thing or another, this and that, this or that
合わす,あわす – to join together, to face, to unite, to be opposite, to combine, to connect, to add up, to mix, to match, to
合わせ,あわせ – joint together, opposite, facing
慌ただしい,あわただしい – busy, hurried, confused, flurried
慌てる,あわてる – to become confused (disconcerted disorganized)
暗殺,あんさつ – assassination
暗算,あんざん – mental arithmetic
暗示,あんじ – hint, suggestion
案じる,あんじる – to be anxious, to ponder
安静,あんせい – rest
案の定,あんのじょう – sure enough, as usual
余り,あんまり – not very (this form only used as adverb), not much, remainder, rest, remnant, surplus, balance, excess, rema
依,い – depending on
良い,いい – good
伊井,いい – that one, Italy
否,いいえ – no, nay, yes, well
いい加減,いいかげん – moderate, right, random, not thorough, vague, irresponsible, halfhearted
言い訳,いいわけ – excuse, explanation
家出,いえで – running away from home, leaving home
家主,いえぬし – landlord
如何,いかが – how, in what way
生かす,いかす – to revive, to resuscitate, to make use of
雷,いかずち – thunder
如何に,いかに – how?, in what way?, how much?, however, whatever
如何にも,いかにも – indeed, really, phrase meaning agreement
怒り,いかり – anger, hatred
怒る,いかる – to get angry, to be angry
歪む,いがむ – to warp, to swerve, to deflect, to be crooked, to be distorted, to be bent, to incline, to slant, to be perv
粋,いき – chic, style, purity, essence
域外,いきがい – outside the area
意気込む,いきごむ – to be enthusiastic about
経緯,いきさつ – 1. details, whole story, sequence of events, particulars, how it started, how things got this way, 2. c
行き違い,いきちがい – misunderstanding, estrangement, disagreement, crossing without meeting, going astray
行き成り,いきなり – suddenly
異議,いぎ – objection, dissent, protest
,いく – to come, to orgasm
軍,いくさ – war, battle, campaign, fight
戦,いくさ – war, battle, campaign, fight
育成,いくせい – rearing, training, nurture, cultivation, promotion
幾多,いくた – many, numerous
活ける,いける – to arrange (flowers)
異見,いけん – different opinion, objection
意向,いこう – intention, idea, inclination
移行,いこう – switching over to
,いざ – now, come (now), well, crucial moment
碑,いしぶみ – stone monument bearing an inscription
衣装,いしょう – clothing, costume, outfit, garment, dress
意地,いじ – disposition, spirit, willpower, obstinacy, backbone, appetite
苛める,いじめる – to tease, to torment, to persecute, to chastise
移住,いじゅう – migration, immigration
弄る,いじる – to touch, to tamper with
何れ,いずれ – where, which, who, anyway, anyhow, at any rate
異性,いせい – the opposite sex
遺跡,いせき – historic ruins (remains relics)
依然,いぜん – still, as yet
依存,いそん – dependence, dependent, reliance
委託,いたく – consign (goods (for sale) to a firm), entrust (person with something), commit
悪戯,いたずら – tease, prank, trick, practical joke, mischief
頂,いただき – (top of) head, summit, spire
戴きます,いただきます – expression of gratitude before meals
至って,いたって – very much, exceedingly, extremely
痛む,いたむ – to hurt, to feel a pain, to be injured
痛める,いためる – to hurt, to injure, to cause pain, to worry, to bother, to afflict, to be grieved over
炒める,いためる – to stir-fry
労る,いたわる – to pity, to sympathize with, to console, to care for, to be kind to
市,いち – market, fair
位地,いち – place, situation, position, location
一々,いちいち – one by one, separately
一概に,いちがいに – unconditionally, as a rule
一見,いちげん – unfamiliar, never before met
一言,いちげん – single word
一日,いちじつ – (1) one day, (2) first of month
一定,いちじょう – fixed, settled, definite, uniform, regularized, defined, standardized, certain, prescribed
著しい,いちじるしい – remarkable, considerable
一同,いちどう – all present, all concerned, all of us
一人,いちにん – one person
一部,いちぶ – 1. one copy e.g. of a document, 2. a part, partly, some
一部分,いちぶぶん – a part
一別,いちべつ – parting
一面,いちめん – one side, one phase, front page, the other hand, the whole surface
一目,いちもく – a glance, a look, a glimpse
一様,いちよう – uniformity, evenness, similarity, equality, impartiality
一律,いちりつ – evenness, uniformity, monotony, equality
一連,いちれん – a series, a chain, a ream (of paper)
一括,いっかつ – all together, batch, one lump, one bundle, summing up
一気,いっき – drink!(said repeatedly as a party cheer)
一挙に,いっきょに – at a stroke, with a single swoop
一切,いっさい – all, everything, without exception, the whole, entirely, absolutely
一心,いっしん – one mind, wholeheartedness, the whole heart
,いっそ – rather, sooner, might as well
一帯,いったい – a region, a zone, the whole place
一敗,いっぱい – one defeat
一変,いっぺん – complete change, about-face
何時,いつ – when, how soon
何時か,いつか – sometime, someday, one day, some time or other, the other day, in due course, in time
何時でも,いつでも – (at) any time, always, at all times, never (neg), whenever
何時の間にか,いつのまにか – before one knows, unnoticed, unawares
何時までも,いつまでも – forever, for good, eternally, as long as one likes, indefinitely
何時も,いつも – always, usually, every time, never (with neg. verb)
意図,いと – intention, aim, design
営む,いとなむ – to carry on (e.g. in ceremony), to run a business
暇,いとま – free time, leisure, leave, spare time, farewell
異動,いどう – a change
挑む,いどむ – to challenge, to contend for, to make love to
稲光,いなびかり – (flash of) lightning
古,いにしえ – antiquity, ancient times
祈り,いのり – prayer, supplication
鼾,いびき – snoring
今更,いまさら – now, at this late hour
未だ,いまだ – as yet, hitherto, not yet (neg)
移民,いみん – emigration, immigration, emigrant, immigrant
厭々,いやいや – unwillingly, grudgingly, shaking head in refusal (to children)
卑しい,いやしい – greedy, vulgar, shabby, humble, base, mean, vile
,いやに – awfully, terribly
厭やらしい,いやらしい – detestable, disagreeable
愈々,いよいよ – more and more, all the more, increasingly, at last, beyond doubt
意欲,いよく – will, desire, ambition
苛々,いらいら – getting nervous, irritation
入口,いりくち – entrance, gate, approach, mouth
衣料,いりょう – clothing
威力,いりょく – power, might, authority, influence
入る,いる – to get in, to go in, to come in, to flow into, to set, to set in
衣類,いるい – clothes, clothing, garments
色々,いろいろ – various
異論,いろん – different opinion, objection
所謂,いわゆる – the so-called, so to speak
印,いん – seal, stamp, mark, print
員,いん – member
印鑑,いんかん – stamp, seal
陰気,いんき – gloom, melancholy
隠居,いんきょ – retirement, retired person
上下,うえした – high and low, up and down, unloading and loading, praising and blaming
浮かぶ,うかぶ – to float, to rise to surface, to come to mind
受かる,うかる – to pass (examination)
含嗽,うがい – gargle, rinse mouth
受け入れ,うけいれ – receiving, acceptance
受け入れる,うけいれる – to accept, to receive
受け継ぐ,うけつぐ – to inherit, to succeed, to take over
受け付ける,うけつける – to be accepted, to receive (an application)
受け止める,うけとめる – to catch, to stop the blow, to react to, to take
受け取り,うけとり – receipt
受身,うけみ – passive, passive voice
動き,うごき – movement, activity, trend, development, change
潮,うしお – tide
氏,うじ – family name
渦,うず – swirl
埋まる,うずまる – to be buried, to be surrounded, to overflow, to be filled
嘘つき,うそつき – liar (sometimes said with not much seriousness), fibber
打ち合わせ,うちあわせ – business meeting, previous arrangement, appointment
打ち合わせる,うちあわせる – to knock together, to arrange
打ち切る,うちきる – to stop, to abort, to discontinue, to close
打ち消し,うちけし – negation, denial, negative
打ち込む,うちこむ – to drive in (e.g. nail stake), to devote oneself to, to shoot into, to smash, to throw into, to cast int
団扇,うちわ – fan
内訳,うちわけ – the items, breakdown, classification
訴え,うったえ – lawsuit, complaint
鬱陶しい,うっとうしい – gloomy, depressing
写し,うつし – copy, duplicate, facsimile, transcript
空ろ,うつろ – blank, cavity, hollow, empty (space)
器,うつわ – bowl, vessel, container
雨天,うてん – rainy weather
腕前,うでまえ – ability, skill, facility
饂飩,うどん – noodles (Japanese)
促す,うながす – to urge, to press, to suggest, to demand, to stimulate, to quicken, to incite, to invite (attention to)
唸る,うなる – to groan, to moan, to roar, to howl, to growl, to hum, to buzz, to sough
自惚れ,うぬぼれ – pretension, conceit, hubris
甘い,うまい – delicious
生まれつき,うまれつき – by nature, by birth, native
海路,うみじ – sea route
産む,うむ – to give birth, to deliver, to produce
埋め込む,うめこむ – to bury
梅干,うめぼし – dried plum
末,うら – top end, tip
裏返し,うらがえし – inside out, upside down
売り出し,うりだし – (bargain) sale
売り出す,うりだす – to put on sale, to market, to become popular
潤う,うるおう – to be moist, to be damp, to get wet, to profit by, to be watered, to receive benefits, to favor, to charm, t
五月蝿い,うるさい – noisy, loud, fussy
売れ行き,うれゆき – sales
浮気,うわき – flighty, fickle, wanton, unfaithful
上手,うわて – 1. upper part, upper stream, left side (of a stage), 2. skillful (only in comparisons), dexterity (on
上回る,うわまわる – to exceed
植わる,うわる – to be planted
運営,うんえい – management, administration, operation
,うんざり – tedious, boring, being fed up with
運送,うんそう – shipping, marine transportation
運賃,うんちん – freight rates, shipping expenses, fare
云々,うんぬん – and so on, and so forth, comment
運搬,うんぱん – transport, carriage
運命,うんめい – fate
運輸,うんゆ – transportation
運用,うんよう – making use of, application, investment, practical use
会,え – understanding
重,え – -fold, -ply
,えい – ray (fish)
映写,えいしゃ – projection
英字,えいじ – English letter (character)
衛生,えいせい – health, hygiene, sanitation, medical
映像,えいぞう – reflection, image
英雄,えいゆう – hero, great man
液,えき – liquid, fluid
役,えき – war, campaign, battle
閲覧,えつらん – inspection, reading
獲物,えもの – game, spoils, trophy
襟,えり – neck, collar, lapel, neckband
縁,えん – chance, fate, destiny, relation, bonds, connection, karma
塩,えん – salt
艶,えん – charming, fascinating, voluptuous
園,えん – garden (esp. man-made)
円滑,えんかつ – harmony, smoothness
縁側,えんがわ – veranda, porch, balcony, open corridor
沿岸,えんがん – coast, shore
婉曲,えんきょく – euphemistic, circumlocution, roundabout, indirect, insinuating
演習,えんしゅう – practice, exercises, manoeuvers
演出,えんしゅつ – production (e.g. play), direction
演じる,えんじる – to perform (a play), to play (a part), to act (a part), to commit (a blunder)
演ずる,えんずる – to perform, to play
沿線,えんせん – along railway line
縁談,えんだん – marriage proposal, engagement
遠方,えんぽう – long way, distant place
円満,えんまん – perfection, harmony, peace, smoothness, completeness, satisfaction, integrity
尾,お – tail, ridge
於,お – at, in, on
甥,おい – nephew
追い込む,おいこむ – to herd, to corner, to drive
美味しい,おいしい – delicious, tasty
追い出す,おいだす – to expel, to drive out
於いて,おいて – at, in, on
お出でになる,おいでになる – to be
老いる,おいる – to age, to grow old
負う,おう – to bear, to owe
応急,おうきゅう – emergency
黄金,おうごん – gold
黄色,おうしょく – yellow
応募,おうぼ – subscription, application
,おおい – hey!
大方,おおかた – perhaps, almost all, majority
大柄,おおがら – large build, large pattern
大げさ,おおげさ – grandiose, exaggerated
大事,おおごと – important, valuable, serious matter
大ざっぱ,おおざっぱ – rough (as in not precise), broad, sketchy
大筋,おおすじ – outline, summary
大空,おおぞら – heaven, firmament, the sky
大幅,おおはば – full width, large scale, drastic
大水,おおみず – flood
公,おおやけ – official, public, formal, open, governmental
お蔭,おかげ – (your) backing, assistance
お蔭様で,おかげさまで – Thanks to god, thanks to you
可笑しい,おかしい – strange, funny, amusing, ridiculous
犯す,おかす – to commit, to perpetrate, to violate, to rape
侵す,おかす – to invade, to raid, to trespass, to violate, to intrude on
お菜,おかず – side dish, accompaniment for rice dishes
臆病,おくびょう – cowardice, timidity
遅らす,おくらす – to retard, to delay
遅れ,おくれ – delay, lag
起こす,おこす – to raise, to cause, to wake someone
行い,おこない – deed, conduct, behavior, action, asceticism
厳か,おごそか – austere, majestic, dignified, stately, awful, impressive
傲る,おごる – to be proud
長,おさ – chief, head
押さえる,おさえる – to stop, to restrain, to seize, to repress, to suppress, to press down
お先に,おさきに – before, ahead, previously
収まる,おさまる – to be obtained, to end, to settle into, to fit into, to be settled, to be paid, to be delivered
納まる,おさまる – to be obtained, to end, to settle into, to fit into, to be settled, to be paid, to be delivered
治まる,おさまる – to be at peace, to clamp down, to lessen (storm terror anger)
お産,おさん – (giving) birth
教え,おしえ – teachings, precept, lesson, doctrine
押し込む,おしこむ – to push into, to crowd into
惜しむ,おしむ – to be frugal, to value, to regret
お喋り,おしゃべり – chattering, talk, idle talk, chat, chitchat, gossip, chatty, talkative, chatterbox, blabbermouth
お洒落,おしゃれ – smartly dressed, someone smartly dressed, fashion-conscious
押し寄せる,おしよせる – to push aside, to advance on
お祖父さん,おじいさん – grandfather, male senior-citizen
お邪魔します,おじゃまします – Excuse me for disturbing (interrupting) you
雄,おす – male (animal)
お世辞,おせじ – flattery, compliment
襲う,おそう – to attack
遅くとも,おそくとも – at the latest
恐らく,おそらく – perhaps
恐れ,おそれ – fear, horror
恐れ入る,おそれいる – to be filled with awe, to feel small, to be amazed, to be surprised, to be disconcerted, to be sorry, to b
お大事に,おだいじに – Take care of yourself
煽てる,おだてる – to stir up, to instigate, to flatter
落ち込む,おちこむ – to fall into, to feel down (sad)
落ち着き,おちつき – calm, composure
落ち葉,おちば – fallen leaves, leaf litter, defoliation, shedding leaves
落ちる,おちる – to fail (e.g. exam), to fall down, to drop
,おっかない – frightening, huge
仰っしゃる,おっしゃる – to say, to speak, to tell, to talk
乙,おつ – 1. strange, quaint, stylish, chic, spicy, queer, witty, tasty, romantic, 2. 2nd in rank, second sign of the
お使い,おつかい – errand
お手上げ,おてあげ – all over, given in, given up hope, bring to knees
御手洗い,おてあらい – toilet, restroom, lavatory, bathroom (US)
弟,おと – younger brother
落とす,おとす – to drop, to lose, to let fall
訪れる,おとずれる – to visit
大人しい,おとなしい – obedient, docile, quiet
少女,おとめ – daughter, young lady, virgin, maiden, little girl
お供,おとも – attendant, companion
衰える,おとろえる – to become weak, to decline, to wear, to abate, to decay, to wither, to waste away
,おどおど – coweringly, hesitantly
脅かす,おどかす – to threaten, to coerce
脅す,おどす – to threaten, to menace
驚き,おどろき – surprise, astonishment, wonder
同い年,おないどし – of the same age
女子,おなご – woman, girl
お願いします,おねがいします – please
各,おのおの – each, every, either, respectively, severally
自ずから,おのずから – naturally, as a matter of course
お早う,おはよう – Good morning
お祖母さん,おばあさん – grandmother, female senior-citizen
怯える,おびえる – to become frightened, to have a nightmare
夥しい,おびただしい – abundantly, innumerably
帯びる,おびる – to wear, to carry, to be entrusted, to have, to take on, to have a trace of, to be tinged with
覚え,おぼえ – memory, sense, experience
御負け,おまけ – 1. a discount, a prize, 2. something additional, bonus, an extra, 3. an exaggeration
お巡りさん,おまわりさん – policeman (friendly term)
お宮,おみや – Shinto shrine
お襁褓,おむつ – diaper, nappy
お目出度う,おめでとう – (ateji) (int) (uk) Congratulations!, an auspicious occasion!
面,おも – face
思い付き,おもいつき – plan, idea, suggestion
面白い,おもしろい – interesting, amusing
玩具,おもちゃ – toy
重なる,おもなる – main, principal, important
趣,おもむき – meaning, tenor, gist, effect, appearance, taste, grace, charm, refinement
赴く,おもむく – to go, to proceed, to repair to, to become
重役,おもやく – heavy responsibilities, director
重んじる,おもんじる – to respect, to honor, to esteem, to prize
重んずる,おもんずる – to honor, to respect, to esteem, to prize
お休み,おやすみ – holiday, absence, rest, Good night
お八,おやつ – 1. (uk) between meal snack, afternoon refreshment, afternoon tea, 2. mid-day snack
凡そ,およそ – about, roughly, as a rule, approximately
及び,および – and, as well as
及ぶ,およぶ – to reach, to come up to, to amount to, to befall, to happen to, to extend, to match, to equal
織,おり – weave, weaving, woven item
檻,おり – cage, pen, jail cell
折り返す,おりかえす – to turn up, to fold back
織物,おりもの – textile, fabric
織る,おる – to weave
俺,おれ – I (ego) (boastful first-person pronoun)
愚か,おろか – foolish, stupid
疎か,おろそか – neglect, negligence, carelessness
終わる,おわる – to finish, to close
音色,おんいろ – tone color, tone quality, timbre, synthesizer patch
温和,おんわ – gentle, mild, moderate
仮,か – tentative, provisional
科,か – department, section
個,か – article counter
下位,かい – low rank, subordinate, lower order (e.g. byte)
階,かい – -floor (counter), stories
改悪,かいあく – deterioration, changing for the worse
海運,かいうん – maritime, marine transportation
改革,かいかく – reform, reformation, innovation
貝殻,かいがら – shell
階級,かいきゅう – class, rank, grade
海峡,かいきょう – channel
会見,かいけん – interview, audience
介護,かいご – nursing
開催,かいさい – holding a meeting, open an exhibition
回収,かいしゅう – collection, recovery
改修,かいしゅう – repair, improvement
怪獣,かいじゅう – monster
解除,かいじょ – cancellation, rescinding, release, calling off
回送,かいそう – forwarding
階層,かいそう – class, level, stratum, hierarchy
開拓,かいたく – reclamation (of wasteland), cultivation, pioneer
会談,かいだん – conversation, conference, discussion, interview
改定,かいてい – reform
改訂,かいてい – revision
街道,かいどう – highway
介入,かいにゅう – intervention
開発,かいはつ – development, exploitation
海抜,かいばつ – height above sea level
介抱,かいほう – nursing, looking after
解剖,かいぼう – dissection, autopsy
回覧,かいらん – circulation
海流,かいりゅう – ocean current
改良,かいりょう – improvement, reform
回路,かいろ – circuit (electric)
顧みる,かえりみる – to look back, to turn around, to review
省みる,かえりみる – to reflect
返る,かえる – to return, to come back, to go back
顔付き,かおつき – (outward) looks, features, face, countenance, expression
掲げる,かかげる – to publish, to print, to carry (an article), to put up, to hang out, to hoist, to fly (a sail), to float (a
踵,かかと – (shoe) heel
係り,かかり – official, duty, person in charge
課外,かがい – extracurricular
書き取り,かきとり – dictation
書き取る,かきとる – to write down, to take dictation, to take notes
掻き回す,かきまわす – to stir up, to churn, to ransack, to disturb
欠く,かく – to lack, to break, to crack, to chip
角,かく – 1. angle, 2. bishop (shogi)
核,かく – nucleus, kernel
格,かく – status, character, case
佳句,かく – beautiful passage of literature
画,かく – stroke
格差,かくさ – qualitative difference, disparity
拡散,かくさん – scattering, diffusion
各種,かくしゅ – every kind, all sorts
隔週,かくしゅう – every other week
確信,かくしん – conviction, confidence
革新,かくしん – reform, innovation
確定,かくてい – definition (math), decision, settlement
獲得,かくとく – acquisition, possession
確保,かくほ – guarantee, ensure, maintain, insure, secure
革命,かくめい – revolution
確立,かくりつ – establishment
賭け,かけ – betting, gambling, a gamble
掛け,かけ – credit
駆け足,かけあし – running fast, double time
家計,かけい – household economy, family finances
駆けっこ,かけっこ – (foot) race
駆ける,かける – to run (race esp. horse), to gallop, to canter
賭ける,かける – to wager, to bet, to risk, to stake, to gamble
#NAME?
加工,かこう – manufacturing, processing, treatment
化合,かごう – chemical combination
嵩張る,かさばる – to be bulky, to be unwieldy, to grow voluminous
嵩む,かさむ – to pile up, to increase
風車,かざぐるま – 1. windmill, 2. pinwheel
畏まりました,かしこまりました – certainly!
華奢,かしゃ – luxury, pomp, delicate, slender, gorgeous
箇所,かしょ – passage, place, point, part
火傷,かしょう – burn, scald
箇条書き,かじょうがき – itemized form, itemization
噛る,かじる – to chew, to bite (at), to gnaw, to nibble, to munch, to crunch, to have a smattering of
微か,かすか – faint, dim, weak, indistinct, hazy, poor, wretched
霞む,かすむ – to grow hazy, to be misty
化する,かする – to change into, to convert into, to transform, to be reduced, to influence, to improve (someone)
擦る,かする – to touch lightly, to take a percentage (from)
火星,かせい – Mars (planet)
化石,かせき – fossil, petrifaction, fossilization
河川,かせん – rivers
化繊,かせん – synthetic fibres
過疎,かそ – depopulation
過多,かた – excess, superabundance
難い,かたい – difficult, hard
片思い,かたおもい – unrequited love
敵,かたき – enemy, rival
気質,かたぎ – spirit, character, trait, temperament, disposition
片言,かたこと – a smattering, talk like a baby, speak haltingly
片付け,かたづけ – tidying up, finishing
傾く,かたぶく – to incline toward, to slant, to lurch, to heel over, to be disposed to, to trend toward, to be prone to, to
傾ける,かたむける – to incline, to list, to bend, to lean, to tip, to tilt, to slant, to concentrate on, to ruin (a country), to
固める,かためる – to harden, to freeze, to fortify
偏る,かたよる – to be one-sided, to incline, to be partial, to be prejudiced, to lean, to be biased
傍ら,かたわら – beside(s), while, nearby
課題,かだい – subject, theme, task
花壇,かだん – flower bed
家畜,かちく – domestic animals, livestock, cattle
画期,かっき – epoch-making
活発,かっぱつ – vigor, active
且つ,かつ – yet, and
割,かつ – divide, cut, halve, separate, split, rip, break, crack, smash, dilute
嘗て,かつて – once, ever
日付,かづけ – date, dating
門,かど – gate
叶う,かなう – to come true (wish)
叶える,かなえる – to grant (request wish)
金槌,かなづち – 1. (iron) hammer, 2. punishment
鉄棒,かなぼう – iron rod, crowbar, horizontal bar (gymnastics)
可成,かなり – considerably, fairly, quite
加入,かにゅう – becoming a member, joining, entry, admission, subscription, affiliation, adherence, signing
金庫,かねぐら – safe, vault, treasury, provider of funds
予言,かねごと – prediction, promise, prognostication
兼ねて,かねて – simultaneously
下番,かばん – going off duty
下品,かひん – inferior article
華美,かび – pomp, splendor, gaudiness
花粉,かふん – pollen
株式,かぶしき – stock (company)
気触れる,かぶれる – to react to, to be influenced by, to go overboard for
貨幣,かへい – money, currency, coinage
構え,かまえ – posture, pose, style
構える,かまえる – to set up
加味,かみ – seasoning, flavoring
噛み切る,かみきる – to bite off, to gnaw through
過密,かみつ – crowded
瓶,かめ – earthenware pot
かも知れない,かもしれない – may, might, perhaps, may be, possibly
粥,かゆ – (rice) gruel
痒い,かゆい – itchy, itching
揶揄う,からかう – to ridicule, to tease, to banter with, to make fun of
身体,からだ – the body
体付き,からだつき – body build, figure
絡む,からむ – to entangle, to entwine
借り,かり – borrowing, debt, loan
下吏,かり – lower official
加留多,かるた – (pt:) (n) playing cards (pt: carta)
涸れる,かれる – to dry up, to run out
過労,かろう – overwork, strain
辛うじて,かろうじて – barely, narrowly, just manage to do st
側,かわ – side, row, surroundings, part, (watch) case
可愛い,かわいい – pretty, cute, lovely, charming, dear, darling, pet
可愛がる,かわいがる – to love, to be affectionate
可哀想,かわいそう – poor, pitiable, pathetic
可愛らしい,かわいらしい – lovely, sweet
交わす,かわす – to exchange (messages), to dodge, to parry, to avoid, to turn aside
代わる,かわる – to take the place of, to relieve, to be substituted for, to be exchanged, to change places with, to take
代わる代わる,かわるがわる – alternately
乾,かん – heaven, emperor
管,かん – pipe, tube
幹,かん – (tree) trunk
冠,かん – crown, diadem, first, best, peerless, cap, naming, designating, initiating on coming of age, top character ra
観,かん – look, appearance, spectacle
館,かん – house, hall, building, hotel, inn, guesthouse
簡易,かんい – simplicity, easiness, quasi-
感慨,かんがい – strong feelings, deep emotion
寒気,かんき – cold, frost, chill
簡潔,かんけつ – brevity, conciseness, simplicity
還元,かんげん – resolution, reduction, return to origins
刊行,かんこう – publication, issue
慣行,かんこう – customary practice, habit, traditional event
勧告,かんこく – advice, counsel, remonstrance, recommendation
看護,かんご – nursing, (army) nurse
漢語,かんご – Chinese word, Sino-Japanese word
換算,かんさん – conversion, change, exchange
監視,かんし – observation, guarding, inspection, surveillance
慣習,かんしゅう – usual (historical) custom
観衆,かんしゅう – spectators, onlookers, members of the audience
干渉,かんしょう – interference, intervention
感触,かんしょく – sense of touch, feeling, sensation
肝心,かんじん – essential, fundamental, crucial, vital, main
歓声,かんせい – cheer, shout of joy
感染,かんせん – infection, contagion
幹線,かんせん – main line, trunk line
関税,かんぜい – customs, duty, tariff
簡素,かんそ – simplicity, plain
観点,かんてん – point of view
感度,かんど – sensitivity, severity (quake)
幹部,かんぶ – management, (executive) staff, leaders
勘弁,かんべん – pardon, forgiveness, forbearance
完璧,かんぺき – perfection, completeness, flawless
感無量,かんむりょう – deep feeling, inexpressible feeling, filled with emotion
勧誘,かんゆう – invitation, solicitation, canvassing, inducement, persuasion, encouragement
関与,かんよ – participation, taking part in, participating in, being concerned in
慣用,かんよう – common, customary
寛容,かんよう – forbearance, tolerance, generosity
観覧,かんらん – viewing
官僚,かんりょう – bureaucrat, bureaucracy
慣例,かんれい – custom, precedent, of convention
還暦,かんれき – 60th birthday
貫禄,かんろく – presence, dignity
緩和,かんわ – relief, mitigation
蓋,がい – cover, lid, cap
街,がい – ~street, ~quarters
外貨,がいか – imported goods, foreign money
外観,がいかん – appearance, exterior, facade
外相,がいしょう – Foreign Minister
害する,がいする – to injure, to damage, to harm, to kill, to hinder
概説,がいせつ – general statement, outline
該当,がいとう – corresponding, answering to, coming under
街頭,がいとう – in the street
概念,がいねん – general idea, concept, notion
外来,がいらい – imported, outpatient clinic
概略,がいりゃく – outline, summary, gist, in brief
学芸,がくげい – arts and sciences, liberal arts
学士,がくし – university graduate
学説,がくせつ – theory
楽譜,がくふ – score (music)
学歴,がくれき – academic background
崖,がけ – cliff
雅致,がち – artistry, good taste, elegance, grace
,がっくり – heartbroken
合唱,がっしょう – chorus, singing in a chorus
,がっしり – firmly, solidly, tough
合致,がっち – agreement, concurrence, conforming to
,がっちり – solidly built, tightly, shrewd, calculating
月日,がっぴ – (the) date
合併,がっぺい – combination, union, amalgamation, consolidation, merger, coalition, fusion, annexation, affiliation, incorpor
,がる – feel
側,がわ – side, row, surroundings, part, (watch) case
癌,がん – cancer
眼科,がんか – ophthalmology
眼球,がんきゅう – eyeball
眼鏡,がんきょう – spectacles, glasses
頑固,がんこ – stubbornness, obstinacy
願書,がんしょ – written application or petition
頑丈,がんじょう – solid, firm, stout, burly, strong, sturdy
岩石,がんせき – rock
元年,がんねん – first year (of a specific reign)
贋物,がんぶつ – imitation, counterfeit, forgery, sham
元来,がんらい – originally, primarily, essentially, logically, naturally
生,き – pure, undiluted, raw, crude
期,き – period, time
企画,きかく – planning, project
規格,きかく – standard, norm
着飾る,きかざる – to dress up
器官,きかん – organ (of body), instrument
季刊,きかん – quarterly (e.g. magazine)
危害,きがい – injury, harm, danger
気兼ね,きがね – hesitance, diffidence, feeling constraint, fear of troubling someone, having scruples about doing someth
気軽,きがる – cheerful, buoyant, lighthearted
危機,きき – crisis
聞き取り,ききとり – listening comprehension
効き目,ききめ – effect, virtue, efficacy, impression
帰京,ききょう – returning to Tokyo
基金,ききん – fund, foundation
棄権,きけん – abstain from voting, renunciation of a right
喜劇,きげき – comedy, funny show
起源,きげん – origin, beginning, rise
機構,きこう – mechanism, organization
既婚,きこん – marriage, married
記載,きさい – mention, entry
気障,きざ – affectation, conceit, snobbery
兆し,きざし – signs, omen, symptoms
兆,きざし – signs, omen, symptoms
軋む,きしむ – to jar, to creak, to grate
気象,きしょう – weather, climate
期日,きじつ – fixed date, settlement date
記述,きじゅつ – describing, descriptor
奇数,きすう – odd number
築く,きずく – to build, to pile up, to amass
傷付く,きずつく – to be hurt, to be wounded, to get injured
規制,きせい – regulation
汽船,きせん – steamship
寄贈,きそう – donation, presentation
貴族,きぞく – noble, aristocrat
鍛える,きたえる – to forge, to drill, to temper, to train, to discipline
来る,きたる – to come, to arrive, to be due to, to be next, to be forthcoming
気立て,きだて – disposition, nature
,きちっと – exactly, perfectly
几帳面,きちょうめん – methodical, punctual, steady
切っ掛け,きっかけ – chance, start, cue, excuse, motive, impetus, occasion
,きっかり – exactly, precisely
喫茶,きっさ – tea drinking, tea house
,きっちり – precisely, tightly
屹度,きっと – 1. (uk) surely, undoubtedly, certainly, without fail, 2. sternly, severely
,きっぱり – clearly, plainly, distinctly
規定,きてい – regulation, provisions
起点,きてん – starting point
軌道,きどう – orbit, railroad track
甲,きのえ – 1st in rank, first sign of the Chinese calendar, shell, instep, grade A
気配,きはい – indication, market trend, worry
規範,きはん – model, standard, pattern, norm, criterion, example
気品,きひん – aroma
気風,きふう – character, traits, ethos
起伏,きふく – undulation
規模,きぼ – scale, scope, plan, structure
気まぐれ,きまぐれ – whim, caprice, whimsy, fickle, moody, uneven temper
生真面目,きまじめ – too serious, person who is too serious, honesty, sincerity
期末,きまつ – end of term
決まり悪い,きまりわるい – feeling awkward, being ashamed
決まる,きまる – to be decided, to be settled, to look good in (clothes)
記名,きめい – signature, register
脚色,きゃくしょく – dramatization (e.g. film)
脚本,きゃくほん – scenario
客観,きゃっかん – objective
規約,きやく – agreement, rules, code
救援,きゅうえん – relief, rescue, reinforcement
休学,きゅうがく – temporary absence from school, suspension
究極,きゅうきょく – ultimate, final, eventual
窮屈,きゅうくつ – narrow, tight, stiff, rigid, uneasy, formal, constrained
球根,きゅうこん – (plant) bulb
救済,きゅうさい – relief, aid, rescue, salvation, help
給食,きゅうしょく – school lunch, providing a meal
給仕,きゅうじ – office boy (girl), page, waiter
休戦,きゅうせん – truce, armistice
旧知,きゅうち – old friend, old friendship
宮殿,きゅうでん – palace
窮乏,きゅうぼう – poverty
丘陵,きゅうりょう – hill
共,きょう – both, neither (neg), all, and, as well as, including, with, together with, plural ending
供,きょう – offer, present, submit, serve (a meal), supply
驚異,きょうい – wonder, miracle
教員,きょういん – teaching staff
教科,きょうか – subject, curriculum
協会,きょうかい – association, society, organization
共感,きょうかん – sympathy, response
共学,きょうがく – coeducation
協議,きょうぎ – conference, consultation, discussion, negotiation
教訓,きょうくん – lesson, precept, moral instruction
境遇,きょうぐう – environment, circumstances
強行,きょうこう – forcing, enforcement
強硬,きょうこう – firm, vigorous, unbending, unyielding, strong, stubborn
凶作,きょうさく – bad harvest, poor crop
共産,きょうさん – communism
教材,きょうざい – teaching materials
教習,きょうしゅう – training, instruction
郷愁,きょうしゅう – nostalgia, homesickness
教職,きょうしょく – teaching certificate, the teaching profession
享受,きょうじゅ – reception, acceptance, enjoyment, being given
興じる,きょうじる – to amuse oneself, to make merry
強制,きょうせい – obligation, coercion, compulsion, enforcement
共存,きょうそん – coexistence
姉妹,きょうだい – sisters
協調,きょうちょう – co-operation, conciliation, harmony, firm (market) tone
協定,きょうてい – arrangement, pact, agreement
脅迫,きょうはく – threat, menace, coercion, terrorism
共鳴,きょうめい – resonance, sympathy
郷里,きょうり – birth-place, home town
強烈,きょうれつ – strong, intense, severe
共和,きょうわ – republicanism, cooperation
曲,きょく – tune, piece of music
局限,きょくげん – limit, localize
極端,きょくたん – extreme, extremity
居住,きょじゅう – residence
拒絶,きょぜつ – refusal, rejection
拒否,きょひ – denial, veto, rejection, refusal
許容,きょよう – permission, pardon
距離,きょり – distance, range
寄与,きよ – contribution, service
清らか,きよらか – clean, pure, chaste
気楽,きらく – at ease, comfortable
煌びやか,きらびやか – gorgeous, gaudy, dazzling, gay
切り,きり – limits, end, bounds, period, place to leave off, closing sentence, all there is, only, since
桐,きり – paulownia tree
切り替える,きりかえる – to change, to exchange, to convert, to renew, to throw a switch, to replace, to switch over
気流,きりゅう – atmospheric current
奇麗,きれい – pretty, clean, nice, tidy, beautiful, fair
切れ目,きれめ – break, pause, gap, end, rift, interruption, cut, section, notch, incision, end (of a task)
際,きわ – edge, brink, verge, side
木綿,きわた – cotton
極めて,きわめて – exceedingly, extremely
僅,きん – a little, small quantity
近眼,きんがん – nearsightedness, shortsightedness, myopia
緊急,きんきゅう – urgent, pressing, emergency
近々,きんきん – nearness, before long
近郊,きんこう – suburbs, outskirts
均衡,きんこう – equilibrium, balance
近視,きんし – shortsightedness
禁じる,きんじる – to prohibit
禁ずる,きんずる – to forbid, to suppress
勤勉,きんべん – industry, diligence
勤務,きんむ – service, duty, work
禁物,きんもつ – taboo, forbidden thing
勤労,きんろう – labor, exertion, diligent service
議案,ぎあん – legislative bill
戯曲,ぎきょく – play, drama
議決,ぎけつ – resolution, decision, vote
議事堂,ぎじどう – Diet building
犠牲,ぎせい – sacrifice
偽造,ぎぞう – forgery, falsification, fabrication, counterfeiting
議題,ぎだい – topic of discussion, agenda
技能,ぎのう – technical skill, ability, capacity
逆転,ぎゃくてん – (sudden) change, reversal, turn-around, coming from behind (baseball)
行,ぎょう – line, row, verse
業者,ぎょうしゃ – trader, merchant
行政,ぎょうせい – administration
業績,ぎょうせき – achievement, performance, results, work, contribution
業務,ぎょうむ – business, affairs, duties, work
玉,ぎょく – king (shogi)
漁船,ぎょせん – fishing boat
漁村,ぎょそん – fishing village
義理,ぎり – duty, sense of duty, honor, decency, courtesy, debt of gratitude, social obligation
疑惑,ぎわく – doubt, misgivings, distrust, suspicion
吟味,ぎんみ – testing, scrutiny, careful investigation
区,く – ward, district, section
食い違う,くいちがう – to cross each other, to run counter to, to differ, to clash, to go awry
空腹,くうふく – hunger
区画,くかく – division, section, compartment, boundary, area, block
区間,くかん – section (of track etc)
茎,くき – stalk
区切り,くぎり – an end, a stop, punctuation
潜る,くぐる – 1. to drive, to pass through, 2. to evade, to hide, 3. to dive (into or under water), to go undergro
種々,くさぐさ – variety
嚏,くしゃみ – sneeze
旧事,くじ – past events, bygones
籤引,くじびき – lottery, drawn lot
擽ぐったい,くすぐったい – ticklish
草臥れる,くたびれる – to get tired, to wear out
下らない,くだらない – good-for-nothing, stupid, trivial, worthless
件,くだん – example, precedent, the usual, the said, the above-mentioned, (man) in question
口ずさむ,くちずさむ – to hum something, to sing to oneself
嘴,くちばし – beak, bill
朽ちる,くちる – to rot
,くっきり – distinctly, clearly, boldly
屈折,くっせつ – bending, indentation, refraction
くっ付く,くっつく – to adhere to, to keep close to
くっ付ける,くっつける – to attach
覆す,くつがえす – to overturn, to upset, to overthrow, to undermine
諄い,くどい – verbose, importunate, heavy (taste)
国境,くにざかい – national or state border
首飾り,くびかざり – necklace
首輪,くびわ – necklace, choker
組み合わせ,くみあわせ – combination
組み合わせる,くみあわせる – to join together, to combine, to join up
組み込む,くみこむ – to insert, to include, to cut in (printing)
蔵,くら – warehouse, cellar, magazine, granary, godown, depository, treasury, elevator
苦しめる,くるしめる – to torment, to harass, to inflict pain
包む,くるむ – to be engulfed in, to be enveloped by, to wrap up, to tuck in, to pack, to do up, to cover with, to dress i
呉れ呉れも,くれぐれも – repeatedly, sincerely, earnestly
呉れる,くれる – to give, to let one have, to do for one, to be given
玄人,くろうと – expert, professional, geisha, prostitute
黒字,くろじ – balance (figure) in the black
君主,くんしゅ – ruler, monarch
愚痴,ぐち – idle complaint, grumble
,ぐっと – firmly, fast, much, more
,ぐらい – approximately
群,ぐん – group (math)
軍艦,ぐんかん – warship, battleship
群集,ぐんしゅう – (social) group, crowd, throng, mob, multitude
軍事,ぐんじ – military affairs
軍備,ぐんび – armaments, military preparations
軍服,ぐんぷく – military or naval uniform
刑,けい – penalty, sentence, punishment
頃,けい – time, about, toward, approximately (time)
傾,けい – lean, incline
系,けい – system, lineage, group
経過,けいか – passage, expiration, progress
軽快,けいかい – rhythmical (e.g. melody), casual (e.g. dress), light, nimble
警戒,けいかい – warning, admonition, vigilance
計器,けいき – meter, gauge
契機,けいき – opportunity, chance
敬具,けいぐ – Sincerely yours
軽減,けいげん – abatement
掲載,けいさい – appearance (e.g. article in paper)
傾斜,けいしゃ – inclination, slant, slope, bevel, list, dip
形成,けいせい – formation
形勢,けいせい – condition, situation, prospects
軽率,けいそつ – rash, thoughtless, careless, hasty
携帯,けいたい – carrying something
形態,けいたい – form, shape, figure
刑罰,けいばつ – judgement, penalty, punishment
経費,けいひ – expenses, cost, outlay
警部,けいぶ – police inspector
軽蔑,けいべつ – scorn, disdain
経歴,けいれき – personal history, career
経路,けいろ – course, route, channel
汚す,けがす – to disgrace, to dishonour
汚らわしい,けがらわしい – filthy, unfair
汚れ,けがれ – uncleanness, impurity, disgrace
汚れる,けがれる – to get dirty, to become dirty
獣,けだもの – beast, brute
吝嗇,けち – stinginess, miser, miserliness, skinflint, tightwad, niggard, pinching pennies
結核,けっかく – tuberculosis, tubercule
血管,けっかん – blood vessel
決行,けっこう – doing (with resolve), carrying out (i.e. a plan)
決算,けっさん – balance sheet, settlement of accounts
決勝,けっしょう – decision of a contest, finals (in sports)
結晶,けっしょう – crystal, crystallization
結成,けっせい – formation
結束,けっそく – union, unity
傑,けつ – excellence
決意,けつい – decision, determination
決議,けつぎ – resolution, vote, decision
結合,けつごう – combination, union
決断,けつだん – decision, determination
欠乏,けつぼう – want, shortage, famine
蹴飛ばす,けとばす – to kick away, to kick off, to kick (someone), to refuse, to reject
貶す,けなす – to speak ill of
煙たい,けむたい – smoky, feeling awkward
煙る,けむる – to smoke (e.g. fire)
家来,けらい – retainer, retinue, servant
,けれど – but, however
圏,けん – sphere, circle, range
権,けん – authority, the right (to do something)
権威,けんい – authority, power, influence
兼業,けんぎょう – side line, second business
権限,けんげん – power, authority, jurisdiction
健在,けんざい – in good health, well
懸賞,けんしょう – offering prizes, winning, reward
検事,けんじ – public prosecutor
健全,けんぜん – health, soundness, wholesome
見地,けんち – point of view
賢明,けんめい – wisdom, intelligence, prudence
倹約,けんやく – thrift, economy, frugality
兼用,けんよう – multi-use, combined use, combination, serving two purposes
権力,けんりょく – power, authority, influence
劇団,げきだん – troupe, theatrical company
激励,げきれい – encouragement
月謝,げっしゃ – monthly tuition fee
,げっそり – being disheartened, losing weight
月賦,げっぷ – monthly installment
下痢,げり – diarrhoea
原,げん – original, primitive, primary, fundamental, raw
原形,げんけい – original form, base form
現行,げんこう – present, current, in operation
原作,げんさく – original work
原子,げんし – atom
元首,げんしゅ – ruler, sovereign
原書,げんしょ – original document
減少,げんしょう – decrease, reduction, decline
現場,げんじょう – actual spot, scene, scene of the crime
元素,げんそ – chemical element
原則,げんそく – principle, general rule
現像,げんぞう – developing (film)
現地,げんち – actual place, local
限定,げんてい – limit, restriction
原点,げんてん – origin (coordinates), starting point
原典,げんてん – original (text)
減点,げんてん – subtract, give a demerit
原爆,げんばく – atomic bomb
原文,げんぶん – the text, original
厳密,げんみつ – strict, close
原油,げんゆ – crude oil
言論,げんろん – discussion
故,こ – the late (deceased)
戸,こ – counter for houses
児,こ – child, the young of animals
巨,こ – big, large, great
恋する,こいする – to fall in love with, to love
溝,こう – 10^38, hundred undecillion (American), hundred sextillion (British)
校,こう – -school, proof
好意,こうい – good will, favor, courtesy
行為,こうい – act, deed, conduct
行員,こういん – bank clerk
交易,こうえき – trade, commerce
公演,こうえん – public performance
後悔,こうかい – regret, repentance
公開,こうかい – presenting to the public
航海,こうかい – sail, voyage
工学,こうがく – engineering
皇居,こうきょ – Imperial Palace
好況,こうきょう – prosperous conditions, healthy economy
抗議,こうぎ – protest, objection
鉱業,こうぎょう – mining industry
興業,こうぎょう – industrial enterprise
高原,こうげん – tableland, plateau
煌々と,こうこうと – brilliantly, brightly
考古学,こうこがく – archaeology
交互,こうご – mutual, reciprocal, alternate
工作,こうさく – work, construction, handicraft, maneuvering
耕作,こうさく – cultivation, farming
鉱山,こうざん – mine (ore)
講習,こうしゅう – short course, training
交渉,こうしょう – negotiations, discussions, connection
高尚,こうしょう – high, noble, refined, advanced
行進,こうしん – march, parade
香辛料,こうしんりょう – spices
口述,こうじゅつ – verbal statement
控除,こうじょ – subsidy, deduction
向上,こうじょう – elevation, rise, improvement, advancement, progress
降水,こうすい – rainfall, precipitation
洪水,こうずい – flood
公然,こうぜん – open (e.g. secret), public, official
抗争,こうそう – dispute, resistance
構想,こうそう – plan, plot, idea, conception
拘束,こうそく – restriction, restraint
後退,こうたい – retreat, backspace (BS)
光沢,こうたく – brilliance, polish, lustre, glossy finish (of photographs)
公団,こうだん – public corporation
好調,こうちょう – favourable, promising, satisfactory, in good shape
口頭,こうとう – oral
講読,こうどく – reading, translation
購読,こうどく – subscription (e.g. magazine)
購入,こうにゅう – purchase, buy
公認,こうにん – official recognition, authorization, licence, accreditation
光熱費,こうねつひ – cost of fuel and light
荒廃,こうはい – ruin
購買,こうばい – purchase, buy
好評,こうひょう – popularity, favorable reputation
交付,こうふ – delivering, furnishing (with copies)
降伏,こうふく – capitulation, surrender, submission
興奮,こうふん – excitement, stimulation, agitation, arousal
公募,こうぼ – public appeal, public contribution
巧妙,こうみょう – ingenious, skillful, clever, deft
公用,こうよう – government business, public use, public expense
小売,こうり – retail
効率,こうりつ – efficiency
公立,こうりつ – public (institution)
小柄,こがら – short (build)
小切手,こぎって – cheque, check
国産,こくさん – domestic products
国定,こくてい – state-sponsored, national
国土,こくど – realm
告白,こくはく – confession, acknowledgement
国防,こくぼう – national defence
国有,こくゆう – national ownership
国連,こくれん – U.N., United Nations
漕ぐ,こぐ – to row, to scull, to pedal
焦げ茶,こげちゃ – black tea
個々,ここ – individual, one by one
箇箇,ここ – individual, separate
心地,ここち – feeling, sensation, mood
心得,こころえ – knowledge, information
心掛け,こころがけ – readiness, intention, aim
心掛ける,こころがける – to bear in mind, to aim to do
志,こころざし – will, intention, motive
志す,こころざす – to plan, to intend, to aspire to, to set aims (sights on)
心強い,こころづよい – heartening, reassuring
心細い,こころぼそい – helpless, forlorn, hopeless, unpromising, lonely, discouraging, disheartening
試み,こころみ – trial, experiment
試みる,こころみる – to try, to test
快い,こころよい – pleasant, agreeable
凝らす,こごらす – to freeze, to congeal
凝る,こごる – to congeal, to freeze
拵える,こしらえる – to make, to manufacture
孤児,こじ – orphan
拗れる,こじれる – to get complicated, to grow worse
故人,こじん – the deceased, old friend
梢,こずえ – treetop
個性,こせい – individuality, personality, idiosyncrasy
戸籍,こせき – census, family register
小銭,こぜに – coins, small change
固体,こたい – solid (body)
答え,こたえ – answer, response
堪える,こたえる – to bear, to stand, to endure, to put up with, to support, to withstand, to resist, to brave, to be fit for, t
火燵,こたつ – table with heater, (orig) charcoal brazier in a floor well
古代,こだい – ancient times
,こだわる – to fuss over, to be particular about, to be concerned about
誇張,こちょう – exaggeration
滑稽,こっけい – funny, humorous, comical, laughable, ridiculous, joking
国交,こっこう – diplomatic relations
骨董品,こっとうひん – curio
骨,こつ – knack, skill
固定,こてい – fixation
事柄,ことがら – matter, thing, affair, circumstance
悉く,ことごとく – altogether, entirely
言伝,ことづて – declaration, hearsay
殊に,ことに – especially, above all
事によると,ことによると – depending on the circumstances
孤独,こどく – isolation, loneliness, solitude
粉々,こなごな – in very small pieces
此の,この – this
この間,このあいだ – the other day, lately, recently
この頃,このごろ – recently
好ましい,このましい – nice, likeable, desirable
個別,こべつ – particular case
零す,こぼす – to spill
零れる,こぼれる – to overflow, to spill
細やか,こまやか – friendly
混む,こむ – to be crowded
込める,こめる – to include, to put into
篭る,こもる – to seclude oneself, to be confined in, to be implied, to be stuffy
固有,こゆう – characteristic, tradition, peculiar, inherent, eigen-
雇用,こよう – employment (long term), hire
暦,こよみ – calendar, almanac
堪える,こらえる – to bear, to stand, to endure, to put up with, to support, to withstand, to resist, to brave, to be fit for, t
孤立,こりつ – isolation, helplessness
懲りる,こりる – to learn by experience, to be disgusted with
此れ,これ – this
此れ等,これら – these
魂,こん – soul, spirit
根気,こんき – patience, perseverance, energy
根拠,こんきょ – basis, foundation
混血,こんけつ – mixed race, mixed parentage
昆虫,こんちゅう – insect, bug
根底,こんてい – root, basis, foundation
混同,こんどう – confusion, mixing, merger
今日は,こんにちは – hello, good day (daytime greeting id)
今晩は,こんばんは – good evening
根本,こんぽん – origin, source, foundation, root, base, principle
御,ご – go-, honourable
語彙,ごい – vocabulary, glossary
濠,ごう – moat
業,ごう – Buddhist karma, actions committed in a former life
号,ごう – number, issue
合意,ごうい – agreement, consent, mutual understanding
合議,ごうぎ – consultation, conference
強気,ごうぎ – great, grand
合成,ごうせい – synthesis, composition, synthetic, composite, mixed, combined, compound
護衛,ごえい – guard, convoy, escort
語句,ごく – words, phrases
極楽,ごくらく – paradise
ご苦労様,ごくろうさま – Thank you very much for your....
語源,ごげん – word root, word derivation, etymology
誤差,ごさ – error
ご座います,ございます – to be (polite), to exist
ご馳走,ごちそう – feast, treating (someone)
ご馳走さま,ごちそうさま – feast
毎,ごと – each respectively
碁盤,ごばん – Go board
ご無沙汰,ごぶさた – not writing or contacting for a while
誤魔化す,ごまかす – to deceive, to falsify, to misrepresent
御免ください,ごめんください – May I come in?
御免なさい,ごめんなさい – I beg your pardon, excuse me
御覧なさい,ごらんなさい – (please) look, (please) try to do
佐,さ – help
再,さい – re-, again, repeated
差異,さい – difference, disparity
#NAME?
再会,さいかい – another meeting, meeting again, reunion
災害,さいがい – calamity, disaster, misfortune
細菌,さいきん – bacillus, bacterium, germ
細工,さいく – work, craftsmanship, tactics, trick
採掘,さいくつ – mining
採決,さいけつ – vote, roll call
再建,さいけん – rebuilding, reconstruction, rehabilitation
再現,さいげん – reappearance, reproduction, return, revival
採算,さいさん – profit
採集,さいしゅう – collecting, gathering
再生,さいせい – playback, regeneration, resuscitation, return to life, rebirth, reincarnation, narrow escape, reclamation, r
最善,さいぜん – the very best
採択,さいたく – adoption, selection, choice
再発,さいはつ – return, relapse, reoccurrence
栽培,さいばい – cultivation
細胞,さいぼう – cell (biology)
採用,さいよう – use, adopt
遮る,さえぎる – to interrupt, to intercept, to obstruct
囀る,さえずる – to sing, to chirp, to twitter
冴える,さえる – to be clear, to be serene, to be cold, to be skillful
竿,さお – rod, pole (e.g. for drying laundry)
栄える,さかえる – to prosper, to flourish
杯,さかずき – wine cups
逆立ち,さかだち – handstand, headstand
逆上る,さかのぼる – to go back, to go upstream, to make retroactive
盛る,さかる – to prosper, to flourish, to copulate (animals)
差額,さがく – balance, difference, margin
下がる,さがる – to hang down, to abate, to retire, to fall, to step back
一昨昨日,さきおととい – two days before yesterday
先に,さきに – before, earlier than, ahead, beyond, away, previously, recently
詐欺,さぎ – fraud, swindle
作,さく – a work, a harvest
策,さく – plan, policy
柵,さく – fence, paling
削減,さくげん – cut, reduction, curtailment
錯誤,さくご – mistake
作戦,さくせん – military or naval operations, tactics, strategy
作物,さくぶつ – literary work
叫び,さけび – shout, scream, outcry
裂ける,さける – to split, to tear, to burst
捧げる,ささげる – to lift up, to give, to offer, to consecrate, to devote, to sacrifice, to dedicate
差し掛かる,さしかかる – to come near to, to approach
指図,さしず – instruction, mandate
差し出す,さしだす – to present, to submit, to tender, to hold out
差し支える,さしつかえる – to interfere, to hinder, to become impeded
差し引く,さしひく – to deduct
些事,さじ – something small or petty, trifle
授ける,さずける – to grant, to award, to teach
嘸,さぞ – I am sure, certainly, no doubt
定まる,さだまる – to become settled, to be fixed
定める,さだめる – to decide, to establish, to determine
錯覚,さっかく – optical illusion, hallucination
早急,さっきゅう – urgent
察する,さっする – to guess, to sense, to presume, to judge, to sympathize with
,さっと – quickly, suddenly
冊,さつ – counter for books
殺人,さつじん – murder
偖,さて – well, now, then
悟る,さとる – to attain enlightenment, to perceive, to understand, to discern
真実,さな – truth, reality
裁く,さばく – to judge
錆び,さび – rust (colour)
左程,さほど – (not) very, (not) much
様,さま – Mr. or Mrs., manner, kind, appearance
三味線,さみせん – three-stringed Japanese guitar, shamisen
侍,さむらい – Samurai, warrior
然も,さも – with gusto, with satisfaction
作用,さよう – action, operation, effect, function
左様なら,さようなら – good-bye
拐う,さらう – to carry off, to run away with, to kidnap, to abduct
爽やか,さわやか – fresh, refreshing, invigorating, clear, fluent, eloquent
障る,さわる – to hinder, to interfere with, to affect, to do one harm, to be harmful to
酸,さん – acid
,さん – Mr or Mrs
酸化,さんか – oxidation
山岳,さんがく – mountains
産休,さんきゅう – maternity leave
桟橋,さんきょう – wharf, bridge, jetty, pier
参議院,さんぎいん – House of Councillors
産後,さんご – postpartum, after childbirth
産出,さんしゅつ – yield, produce
参照,さんしょう – reference, consultation, consultation
参上,さんじょう – calling on, visiting
賛成,さんせい – approval, agreement, support, favour
賛美,さんび – praise, adoration, glorification
産婦人科,さんふじんか – maternity and gynecology department
産物,さんぶつ – product, result, fruit
山腹,さんぷく – hillside, mountainside
山脈,さんみゃく – mountain range
財,ざい – fortune, riches
財源,ざいげん – source of funds, resources, finances
在庫,ざいこ – stockpile, stock
財政,ざいせい – economy, financial affairs
座談会,ざだんかい – symposium, round-table discussion
雑貨,ざっか – miscellaneous goods, general goods, sundries
雑,ざつ – rough, crude
雑談,ざつだん – chatting, idle talk
雑木,ざつぼく – various kinds of small trees, assorted trees
座標,ざひょう – coordinate(s)
残金,ざんきん – remaining money
残酷,ざんこく – cruelty, harshness
残高,ざんだか – (bank) balance, remainder
死,し – death, decease
,し – 10^24 (kanji is JIS X 0212 kuten 4906), septillion (American), quadrillion (British)
次,し – order, sequence, times, next, below
仕上がり,しあがり – finish, end, completion
仕上げ,しあげ – end, finishing touches, being finished
仕上げる,しあげる – to finish up, to complete
明々後日,しあさって – two days after tomorrow
飼育,しいく – breeding, raising, rearing
強いて,しいて – by force
強いる,しいる – to force, to compel, to coerce
仕入れる,しいれる – to lay in stock, to replenish stock, to procure
,しいんと – silent (as the grave), (deathly) quiet
歯科,しか – dentistry
資格,しかく – qualifications, requirements, capabilities
視覚,しかく – sense of sight, vision
仕掛け,しかけ – device, trick, mechanism, gadget, (small) scale, half finished, commencement, set up, challenge
仕掛ける,しかける – to commence, to lay (mines), to set (traps), to wage (war), to challenge
然し,しかし – however, but
然しながら,しかしながら – nevertheless, however
而も,しかも – moreover, furthermore, nevertheless, and yet
市街,しがい – urban areas, the streets, town, city
指揮,しき – command, direction
色彩,しきさい – colour, hue, tints
式場,しきじょう – ceremonial hall, place of ceremony (e.g. marriage)
為来り,しきたり – customs
頻りに,しきりに – frequently, repeatedly, incessantly, eagerly
仕切る,しきる – to partition, to divide, to mark off, to settle accounts, to toe the mark
資金,しきん – funds, capital
施行,しぎょう – 1. execution, enforcing, carrying out
,しくじる – to fail, to fall through, to blunder
仕組み,しくみ – devising, plan, plot, contrivance, construction, arrangement
死刑,しけい – death penalty, capital punishment
湿気る,しける – to be damp, to be moist
思考,しこう – thought
志向,しこう – intention, aim
嗜好,しこう – taste, liking, preference
視察,しさつ – inspection, observation
資産,しさん – property, fortune, means, assets
刺繍,ししゅう – embroidery
支持,しじ – support, maintenance
指示,しじ – indication, instruction, directions
雫,しずく – drop (of water)
沈める,しずめる – to sink, to submerge
施設,しせつ – institution, establishment, facility, (army) engineer
子息,しそく – son
慕う,したう – to yearn for, to miss, to adore, to love dearly
従って,したがって – therefore, consequently, in accordance with
下心,したごころ – secret intention, motive
親しむ,したしむ – to be intimate with, to befriend
下調べ,したしらべ – preliminary investigation, preparation
下地,したじ – groundwork, foundation, inclination, aptitude, elementary knowledge of, grounding in, prearrangement, spade
認める,したためる – to write up
仕立てる,したてる – to tailor, to make, to prepare, to train, to send (a messenger)
下取り,したどり – trade in, part exchange
下火,したび – burning low, waning, declining
失格,しっかく – disqualification, elimination, incapacity (legal)
確り,しっかり – firmly, tightly, reliable, level-headed, steady
質素,しっそ – simplicity, modesty, frugality
失調,しっちょう – lack of harmony
嫉妬,しっと – jealousy
尻尾,しっぽ – tail (animal)
室,しつ – room
質疑,しつぎ – question
躾,しつけ – home discipline, training, upbringing, breeding
仕付ける,しつける – to be used to a job, to begin to do, to baste, to tack, to plant
指摘,してき – pointing out, identification
視点,してん – opinion, point of view, visual point
萎びる,しなびる – to wilt, to fade
嫋か,しなやか – supple, flexible, elastic
屎尿,しにょう – excreta, raw sewage, human waste, night soil
凌ぐ,しのぐ – to outdo, to surpass, to endure, to keep out (rain), to stave off, to tide over, to pull through, to defy, t
始発,しはつ – first train
芝,しば – lawn, sod, turf
屡,しばしば – often, again and again, frequently
暫く,しばらく – little while
痺れる,しびれる – to become numb, to go to sleep (i.e. a limb)
渋い,しぶい – 1. tasteful (clothing), cool, an aura of refined masculinity, 2. astringent, sullen, bitter (taste), 3
私物,しぶつ – private property, personal effects
,しぶとい – tenacious, stubborn
司法,しほう – administration of justice
脂肪,しぼう – fat, grease, blubber
志望,しぼう – wish, desire, ambition
萎む,しぼむ – to wither, to fade (away), to shrivel, to wilt
仕舞,しまい – end, termination, informal (Noh play)
仕舞う,しまう – to finish, to close, to do something completely, to put away, to put an end to
,しまった – Damn it!
始末,しまつ – management, dealing, settlement, cleaning up afterwards
泌み泌み,しみじみ – keenly, deeply, heartily
染みる,しみる – to pierce, to permeate
使命,しめい – mission, errand, message
締め切り,しめきり – closing, cut-off, end, deadline, Closed, No Entrance
僕,しもべ – manservant, servant (of God)
社交,しゃこう – social life, social intercourse
謝絶,しゃぜつ – refusal
社宅,しゃたく – company owned house
吃逆,しゃっくり – hiccough, hiccup
喋る,しゃべる – to talk, to chat, to chatter
斜面,しゃめん – slope, slanting surface, bevel
洒落,しゃらく – frank, open-hearted
洒落る,しゃれる – to joke, to play on words, to dress stylishly
視野,しや – field of vision, outlook
種,しゅ – kind, variety, species
衆,しゅう – masses, great number, the people
周,しゅう – circuit, lap, circumference, vicinity, Chou (dynasty)
収益,しゅうえき – earnings, proceeds, returns
修学,しゅうがく – learning
周期,しゅうき – cycle, period
衆議院,しゅうぎいん – Lower House, House of Representatives
就業,しゅうぎょう – employment, starting work
修行,しゅうぎょう – pursuit of knowledge, studying, learning, training, ascetic practice, discipline
集計,しゅうけい – totalization, aggregate
襲撃,しゅうげき – attack, charge, raid
収支,しゅうし – income and expenditure
終始,しゅうし – beginning and end, from beginning to end, doing a thing from beginning to end
修士,しゅうし – Masters degree program
収集,しゅうしゅう – gathering up, collection, accumulation
修飾,しゅうしょく – ornamentation, embellishment, decoration, adornment, polish up (writing), modification (gram)
終日,しゅうじつ – all day
執着,しゅうじゃく – attachment, adhesion, tenacity
収容,しゅうよう – accommodation, reception, seating, housing, custody, admission, entering (in a dictionary)
修了,しゅうりょう – completion (of a course)
守衛,しゅえい – security guard, doorkeeper
主演,しゅえん – starring, playing the leading part
主観,しゅかん – subjectivity, subject, ego
祝賀,しゅくが – celebration, congratulations
宿命,しゅくめい – fate, destiny, predestination
主権,しゅけん – sovereignty, supremacy, dominion
手芸,しゅげい – handicrafts
主催,しゅさい – organization, sponsorship
取材,しゅざい – choice of subject, collecting data
趣旨,しゅし – object, meaning
主食,しゅしょく – staple food
主人公,しゅじんこう – protagonist, main character, hero(ine) (of a story), head of household
主体,しゅたい – subject, main constituent
主題,しゅだい – subject, theme, motif
出血,しゅっけつ – bleeding, haemorrhage
出産,しゅっさん – (child)birth, delivery, production (of goods)
出社,しゅっしゃ – arrival (in a country at work etc.)
出生,しゅっしょう – birth
出世,しゅっせ – promotion, successful career, eminence
出費,しゅっぴ – expenses, disbursements
出品,しゅっぴん – exhibit, display
出演,しゅつえん – performance, stage appearance
出題,しゅつだい – proposing a question
出動,しゅつどう – sailing, marching, going out
主導,しゅどう – main leadership
主任,しゅにん – person in charge, responsible official
首脳,しゅのう – head, brains
守備,しゅび – defense
手法,しゅほう – technique
私有,しゆう – private ownership
諸,しょ – various, many, several
背負う,しょう – to be burdened with, to carry on back or shoulder
象,しょう – phenomenon
症,しょう – illness
傷,しょう – wound, injury, hurt, cut, gash, bruise, scratch, scar, weak point
商,しょう – quotient
消去,しょうきょ – elimination, erasing, dying out, melting away
衝撃,しょうげき – shock, crash, impact, ballistic
証言,しょうげん – evidence, testimony
証拠,しょうこ – evidence, proof
消耗,しょうこう – exhaustion, consumption
照合,しょうごう – collation, comparison
詳細,しょうさい – detail, particulars
昇進,しょうしん – promotion
少数,しょうすう – minority, few
称する,しょうする – to pretend, to take the name of, to feign, to purport
消息,しょうそく – news, letter, circumstances
承諾,しょうだく – consent, acquiescence, agreement
象徴,しょうちょう – symbol
小児科,しょうにか – pediatrics
証人,しょうにん – witness
照明,しょうめい – illumination
勝利,しょうり – victory, triumph, conquest, success, win
奨励,しょうれい – encouragement, promotion, message, address
職員,しょくいん – staff member, personnel
植民地,しょくみんち – colony
職務,しょくむ – professional duties
諸君,しょくん – Gentlemen!, Ladies!
所在,しょざい – whereabouts
所々,しょしょ – here and there, some parts (of something)
所持,しょじ – possession, owning
所属,しょぞく – attached to, belong to
処置,しょち – treatment
,しょっちゅう – always, constantly
所定,しょてい – fixed, prescribed
所得,しょとく – income, earnings
初版,しょはん – first edition
処罰,しょばつ – punishment
書評,しょひょう – book review
処分,しょぶん – disposal, dealing, punishment
庶民,しょみん – masses, common people
庶務,しょむ – general affairs
私用,しよう – personal use, private business
仕様,しよう – way, method, resource, remedy, (technical) specification
使用人,しようにん – employee, servant
調べ,しらべ – preparation, investigation, inspection
知り合い,しりあい – acquaintance
退く,しりぞく – to retreat, to recede, to withdraw
退ける,しりぞける – to repel, to drive away
記す,しるす – to note, to write down
指令,しれい – orders, instructions, directive
代,しろ – price, materials, substitution
皺,しわ – wrinkles, creases
新,しん – new
進化,しんか – evolution, progress
殿,しんがり – rear, rear unit guard
審議,しんぎ – deliberation
進行,しんこう – advance
新興,しんこう – rising, developing, emergent
振興,しんこう – promotion, encouragement
申告,しんこく – report, statement, filing a return, notification
新婚,しんこん – newly-wed
審査,しんさ – judging, inspection, examination, investigation
紳士,しんし – gentleman
進出,しんしゅつ – advance, step forward
信者,しんじゃ – believer, adherent, devotee, Christian
真珠,しんじゅ – pearl
心中,しんじゅう – double suicide, lovers suicide
心情,しんじょう – mentality
新人,しんじん – new face, newcomer
神聖,しんせい – holiness, sacredness, dignity
親善,しんぜん – friendship
真相,しんそう – truth, real situation
新築,しんちく – new building, new construction
進呈,しんてい – presentation
進展,しんてん – progress, development
神殿,しんでん – temple, sacred place
進度,しんど – progress
振動,しんどう – oscillation, vibration
新入生,しんにゅうせい – freshman, first-year student
信任,しんにん – trust, confidence, credence
審判,しんばん – refereeing, trial, judgement, umpire, referee
神秘,しんぴ – mystery
辛抱,しんぼう – patience, endurance
真理,しんり – truth
侵略,しんりゃく – aggression, invasion, raid
診療,しんりょう – medical examination and treatment, diagnosis
進路,しんろ – course, route
自覚,じかく – self-conscious
地方,じかた – area, locality, district, region, the coast
自我,じが – self, the ego
磁気,じき – magnetism
磁器,じき – porcelain, china
事業,じぎょう – project, enterprise, business, industry, operations
地形,じぎょう – terrain, geographical features, topography
軸,じく – axis, stem, shaft, axle
自己,じこ – self, oneself
事項,じこう – matter, item, facts
時刻表,じこくひょう – table, diagram, chart, timetable, schedule
地獄,じごく – hell
時差,じさ – time difference
自在,じざい – freely, at will
自主,じしゅ – independence, autonomy
自首,じしゅ – surrender, give oneself up
辞職,じしょく – resignation
自信,じしん – self-confidence
事前,じぜん – prior, beforehand, in advance
自尊心,じそんしん – self-respect, conceit
持続,じぞく – continuation
字体,じたい – type, font, lettering
辞退,じたい – refusal
,じっくり – deliberately, carefully
実質,じっしつ – substance, essence
実践,じっせん – practice, put into practice
実態,じったい – truth, fact
実費,じっぴ – actual expense, cost price
十分,じっぷん – 10 minutes
実,じつ – truth, reality, sincerity, fidelity, kindness, faith, substance, essence
実業家,じつぎょうか – industrialist, businessman
実情,じつじょう – real condition, actual circumstances, actual state of affairs
自転,じてん – rotation, spin
自動詞,じどうし – intransitive verb (no direct obj)
地主,じぬし – landlord
耳鼻科,じびか – otolaryngology
地元,じもと – local
弱,じゃく – weakness, the weak, little less then
若干,じゃっかん – some, few, number of
砂利,じゃり – gravel, ballast, pebbles
じゃん拳,じゃんけん – rock-scissors-paper game
住,じゅう – dwelling, living
従業員,じゅうぎょういん – employee, worker
従事,じゅうじ – engaging, pursuing, following
充実,じゅうじつ – fullness, completion, perfection, substantiality, enrichment
十字路,じゅうじろ – crossroads
絨毯,じゅうたん – carpet
柔軟,じゅうなん – flexible, lithe
重複,じゅうふく – duplication, repetition, overlapping, redundancy, restoration
重宝,じゅうほう – priceless treasure, convenience, usefulness
従来,じゅうらい – up to now, so far, traditional
塾,じゅく – coaching school, lessons
樹木,じゅもく – trees and shrubs, arbour
樹立,じゅりつ – establish, create
準急,じゅんきゅう – local express (train slower than an express)
準じる,じゅんじる – to follow, to conform, to apply to
準ずる,じゅんずる – to apply correspondingly, to correspond to, to be proportionate to, to conform to
助,じょ – help, rescue, assistant
情,じょう – feelings, emotion, passion
#NAME?
尉,じょう – jailer, old man, rank, company officer
嬢,じょう – young woman
状,じょう – shape
上位,じょうい – superior (rank not class), higher order (e.g. byte), host computer (of connected device)
上演,じょうえん – performance (e.g. music)
城下,じょうか – land near the castle
乗客,じょうかく – passenger
上空,じょうくう – sky, the skies, high-altitude sky, upper air
上司,じょうし – superior authorities, boss
情緒,じょうしょ – emotion, feeling
上昇,じょうしょう – rising, ascending, climbing
情勢,じょうせい – state of things, condition, situation
情熱,じょうねつ – passion, enthusiasm, zeal
丈夫,じょうふ – 1. hero, gentleman, warrior, manly person, 2. good health, robustness, strong, solid, durable
譲歩,じょうほ – concession, conciliation, compromise
条約,じょうやく – treaty, pact
上陸,じょうりく – landing, disembarkation
蒸留,じょうりゅう – distillation
除外,じょがい – exception, exclusion
助言,じょげん – advice, suggestion
徐行,じょこう – going slowly
女史,じょし – Ms.
助詞,じょし – particle, postposition
助動詞,じょどうし – auxiliary verb
自立,じりつ – independence, self-reliance
人,じん – man, person, people
人格,じんかく – personality, character, individuality
人材,じんざい – man of talent
迅速,じんそく – quick, fast, rapid, swift, prompt
人体,じんたい – human body
人民,じんみん – people, public
人目,じんもく – glimpse, public gaze
水気,すいき – 1. moisture, dampness, vapor, 2. dropsy, edema
水源,すいげん – source of river, fountainhead
推進,すいしん – propulsion, driving force
水洗,すいせん – flushing
吹奏,すいそう – playing wind instruments
推測,すいそく – guess, conjecture
水田,すいでん – (water-filled) paddy field
推理,すいり – reasoning, inference, mystery or detective genre (movie novel etc.)
数詞,すうし – numeral
崇拝,すうはい – worship, adoration, admiration, cult
据え付ける,すえつける – to install, to equip, to mount
据える,すえる – to set (table), to lay (foundation), to place (gun), to apply (moxa)
清々しい,すがすがしい – fresh, refreshing
過ぎ,すぎ – past, after
救い,すくい – help, aid, relief
掬う,すくう – to scoop, to ladle out
少なくとも,すくなくとも – at least
直ぐ,すぐ – immediately, soon, easily, right (near), honest, upright
健やか,すこやか – vigorous, healthy, sound
濯ぐ,すすぐ – to rinse, to wash out
進み,すすみ – progress
勧め,すすめ – recommendation, advice, encouragement
裾,すそ – (trouser) cuff, (skirt) hem, cut edge of a hairdo, foot of mountain
廃れる,すたれる – to go out of use, to become obsolete, to die out, to go out of fashion
酸っぱい,すっぱい – sour, acid
素敵,すてき – lovely, dreamy, beautiful, great, fantastic, superb, cool, capital
即ち,すなわち – that is, namely, i.e.
,すばしこい – nimble, smart, quick
素早い,すばやい – fast, quick, prompt, agile
済ます,すます – to finish, to get it over with, to settle, to conclude, to pay back
澄ます,すます – to clear, to make clear, to be unruffled, to look unconcerned, to look demure, look prim, put on airs
済まない,すまない – sorry (phrase)
済みません,すみません – sorry, excuse me
天皇,すめらぎ – Emperor of Japan
刷り,すり – printing
剃る,する – to shave
擦れ違い,すれちがい – chance encounter
すれ違う,すれちがう – to pass by one another, to disagree, to miss each other
擦れる,すれる – to rub, to chafe, to wear, to become sophisticated
,すんなり – pass with no objection, slim, slender
図々しい,ずうずうしい – impudent, shameless
,ずばり – decisively, decidedly, once and for all, unreservedly, frankly
ずぶ濡れ,ずぶぬれ – soaked, dripping wet
,ずらっと – in a line, in a row
,ずるずる – sound or act of dragging, loose, inconclusive but unwanted situation, trailingly
,ずれ – gap, slippage
,ずれる – to slide, to slip off
制,せい – system, organization, imperial command, laws, regulation, control, government, suppression, restraint, holdin
製,せい – -made, make
生育,せいいく – growth, development, breeding
成果,せいか – results, fruits
正解,せいかい – correct, right, correct interpretation (answer solution)
正規,せいき – regular, legal, formal, established, legitimate
正義,せいぎ – justice, right, righteousness, correct meaning
生計,せいけい – livelihood, living
政権,せいけん – administration, political power
精巧,せいこう – elaborate, delicate, exquisite
制裁,せいさい – restraint, sanctions, punishment
政策,せいさく – political measures, policy
清算,せいさん – liquidation, settlement
星座,せいざ – constellation
生死,せいし – life and death
静止,せいし – stillness, repose, standing still
青春,せいしゅん – youth, springtime of life, adolescent
聖書,せいしょ – Bible, scriptures
誠実,せいじつ – sincere, honest, faithful
成熟,せいじゅく – maturity, ripeness
清純,せいじゅん – purity, innocence
正常,せいじょう – normalcy, normality, normal
制する,せいする – to control, to command, to get the better of
整然,せいぜん – orderly, regular, well-organized, trim, accurate
盛装,せいそう – be dressed up, wear rich clothes
盛大,せいだい – grand, prosperous, magnificent
清濁,せいだく – good and evil, purity and impurity
制定,せいてい – enactment, establishment, creation
静的,せいてき – static
製鉄,せいてつ – iron manufacture
晴天,せいてん – fine weather
正当,せいとう – just, justifiable, right, due, proper, equitable, reasonable, legitimate, lawful
成年,せいねん – majority, adult age
制服,せいふく – uniform
征服,せいふく – conquest, subjugation, overcoming
製法,せいほう – manufacturing method, recipe, formula
精密,せいみつ – precise, exact, detailed, minute, close
声明,せいめい – declaration, statement, proclamation
姓名,せいめい – full name
制約,せいやく – limitation, restriction, condition, constraints
生理,せいり – physiology, menses
勢力,せいりょく – influence, power, might, strength, potency, force, energy
整列,せいれつ – stand in a row, form a line
急かす,せかす – to hurry, to urge on
伜,せがれ – son, my son
責務,せきむ – duty, obligation
世辞,せじ – flattery, compliment
世帯,せたい – household
世代,せだい – generation, the world, the age
切開,せっかい – clearing (land), opening up, cutting through
接触,せっしょく – touch, contact
設置,せっち – establishment, institution
折衷,せっちゅう – compromise, cross, blending, eclecticism
設定,せってい – establishment, creation
説得,せっとく – persuasion
節,せつ – node, section, occasion, time
切実,せつじつ – compelling, serious, severe, acute, earnest, pressing, urgent
接続詞,せつぞくし – conjunction
切ない,せつない – painful, trying, oppressive, suffocating
設立,せつりつ – establishment, foundation, institution
攻め,せめ – attack, offence
世論,せろん – public opinion
仙,せん – hermit, wizard
前,せん – before
繊維,せんい – fibre, fiber, textile
選挙,せんきょ – election
宣教,せんきょう – religious mission
宣言,せんげん – declaration, proclamation, announcement
先行,せんこう – preceding, going first
選考,せんこう – selection, screening
戦災,せんさい – war damage
専修,せんしゅう – specialization
戦術,せんじゅつ – tactics
潜水,せんすい – diving
先先月,せんせんげつ – month before last
先先週,せんせんしゅう – week before last
先代,せんだい – family predecessor, previous age, previous generation
先だって,せんだって – recently, the other day
先着,せんちゃく – first arrival
先天的,せんてんてき – a priori, inborn, innate, inherent, congenital, hereditary
戦闘,せんとう – battle, fight, combat
潜入,せんにゅう – infiltration, sneaking in
船舶,せんぱく – ship
専用,せんよう – exclusive use, personal use
占領,せんりょう – occupation, capture, possession, have a room to oneself
戦力,せんりょく – war potential
税務署,ぜいむしょ – tax office
是正,ぜせい – correction, revision
絶版,ぜっぱん – out of print
絶望,ぜつぼう – despair, hopelessness
是非とも,ぜひとも – by all means (with sense of not taking no for an answer)
膳,ぜん – (small) table, tray, meal
禅,ぜん – Zen (Buddhism)
全快,ぜんかい – complete recovery of health
全盛,ぜんせい – height of prosperity
前提,ぜんてい – preamble, premise, reason, prerequisite
前途,ぜんと – future prospects, outlook, the journey ahead
全滅,ぜんめつ – annihilation
善良,ぜんりょう – goodness, excellence, virtue
前例,ぜんれい – precedent
僧,そう – monk, priest
沿う,そう – to run along, to follow
添う,そう – to accompany, to become married, to comply with
総,そう – whole, all, general, gross
相応,そうおう – suitability, fitness
総会,そうかい – general meeting
創刊,そうかん – launching (e.g. newspaper), first issue
送金,そうきん – remittance, sending money
走行,そうこう – running a wheeled vehicle (e.g. car), traveling
総合,そうごう – synthesis, coordination, putting together, integration, composite
捜査,そうさ – search (esp. in criminal investigations), investigation
捜索,そうさく – search (esp. for someone or something missing), investigation
然うして,そうして – and, like that
装飾,そうしょく – ornament
操縦,そうじゅう – management, handling, control, manipulation
創造,そうぞう – creation
壮大,そうだい – magnificent, grand, majestic, splendid
騒動,そうどう – strife, riot, rebellion
遭難,そうなん – disaster, shipwreck, accident
相場,そうば – market price, speculation, estimation
装備,そうび – equipment
創立,そうりつ – establishment, founding, organization
添える,そえる – to add to, to attach, to append, to accompany, to garnish, to imitate, to annex
即座に,そくざに – immediately, right away
促進,そくしん – promotion, acceleration, encouragement, facilitation, spurring on
即する,そくする – to conform to, to agree with, to be adapted to, to be based on
束縛,そくばく – restraint, shackles, restriction, confinement, binding
側面,そくめん – side, flank, sidelight, lateral
其処,そこ – that place, there
其処で,そこで – so (conj), accordingly, now, then, thereupon
損なう,そこなう – to harm, to hurt, to injure, to damage, to fail in doing
其処ら,そこら – everywhere, somewhere, approximately, that area, around there
素材,そざい – raw materials, subject matter
阻止,そし – obstruction, check, hindrance, prevention, interdiction
然して,そして – and
訴訟,そしょう – litigation, lawsuit
育ち,そだち – breeding, growth
措置,そち – measure, step
其方,そちら – over there, the other
素っ気ない,そっけない – cold, short, curt, blunt
率直,そっちょく – frankness, candour, openheartedness
外方,そっぽ – look (or turn) the other way
備え付ける,そなえつける – to provide, to furnish, to equip, to install
備わる,そなわる – to be furnished with, to be endowed with, to possess, to be among, to be one of, to be possessed of
園,その – garden, park, plantation
その上,そのうえ – in addition, furthermore
その内,そのうち – eventually, sooner or later, of the previously mentioned
その為,そのため – hence, for that reason
その外,そのほか – besides, in addition, the rest
其の儘,そのまま – without change, as it is (i.e. now)
聳える,そびえる – to rise, to tower, to soar
素朴,そぼく – simplicity, artlessness, naivete
染まる,そまる – to dye
背く,そむく – to run counter to, to go against, to disobey, to infringe
染める,そめる – to dye, to colour
逸らす,そらす – to turn away, to avert
反り,そり – warp, curvature, curve, arch
其れ,それ – it, that
其れから,それから – and then, after that
各々,それぞれ – each, every, either, respectively, severally
其れで,それで – and (conj), thereupon, because of that
其れでは,それでは – in that situation, well then ...
其れでも,それでも – but (still), and yet, nevertheless, even so, notwithstanding
其れ共,それとも – or, or else
其れに,それに – besides, moreover
其れ程,それほど – to that degree, extent
其れ故,それゆえ – therefore, for that reason, so
揃い,そろい – set, suit, uniform
徐々,そろそろ – gradually, steadily, quietly, slowly, soon
損失,そんしつ – loss
存続,そんぞく – duration, continuance
沿い,ぞい – along
像,ぞう – statue, image, figure, picture, portrait
増強,ぞうきょう – augment, reinforce, increase
蔵相,ぞうしょう – Minister of Finance
増進,ぞうしん – promoting, increase, advance
,ぞんざい – rude, careless, slovenly
他意,たい – ill will, malice, another intention, secret purpose, ulterior motive, fickleness, double-mindedness
対応,たいおう – interaction, correspondence, coping with, dealing with
退化,たいか – degeneration, retrogression
体格,たいかく – physique, constitution
大概,たいがい – in general, mainly
退学,たいがく – dropping out of school
大金,たいきん – great cost
待遇,たいぐう – treatment, reception
対決,たいけつ – confrontation, showdown
体験,たいけん – personal experience
対抗,たいこう – opposition, antagonism
対して,たいして – for, in regard to, per
大衆,たいしゅう – general public
対処,たいしょ – deal with, cope
退職,たいしょく – retirement (from office)
退治,たいじ – extermination
態勢,たいせい – attitude, conditions, preparations
対談,たいだん – talk, dialogue, conversation
対等,たいとう – equivalent
滞納,たいのう – non-payment, default
対比,たいひ – contrast, comparison
大部,たいぶ – most (e.g. most part), greater, fairly, a good deal, much
対辺,たいへん – (geometrical) opposite side
待望,たいぼう – expectant waiting
怠慢,たいまん – negligence, procrastination, carelessness
対面,たいめん – interview, meeting
対立,たいりつ – confrontation, opposition, antagonism
体力,たいりょく – physical strength
対話,たいわ – interactive, interaction, conversation, dialogue
耐える,たえる – to bear, to endure
絶える,たえる – to die out, to peter out, to become extinct
堪える,たえる – to bear, to stand, to endure, to put up with, to support, to withstand, to resist, to brave, to be fit for, t
高,たか – quantity, amount, volume, number, amount of money
高まる,たかまる – to rise, to swell, to be promoted
焚火,たきび – (open) fire
沢山,たくさん – many, a lot, much
逞しい,たくましい – burly, strong, sturdy
巧み,たくみ – skill, cleverness
類,たぐい – a kind
丈,たけ – height, stature, length, measure, all (one has)
足し算,たしざん – addition
多数決,たすうけつ – majority rule
助け,たすけ – assistance
携わる,たずさわる – to participate, to take part
漂う,ただよう – to drift about, to float, to hang in air
館,たち – 1. mansion, small castle
立方,たちかた – dancing (geisha)
忽ち,たちまち – at once, in a moment, suddenly, all at once
立ち寄る,たちよる – to stop by, to drop in for a short visit
達者,たっしゃ – skillful, in good health
達成,たっせい – achievement
,たった – only, merely, but, no more than
尊い,たっとい – precious, valuable, priceless, noble, exalted, sacred
貴い,たっとい – precious, valuable, priceless, noble, exalted, sacred
尊ぶ,たっとぶ – to value, to prize, to esteem
絶つ,たつ – to sever, to cut off, to suppress, to abstain (from)
盾,たて – shield, buckler, escutcheon, pretext
建前,たてまえ – face, official stance, public position or attitude (as opposed to private thoughts)
奉る,たてまつる – to offer, to present, to revere, to do respectfully
例え,たとえ – example, even if, if, though, although
仮令,たとえ – example, even if, if, though, although
他動詞,たどうし – transitive verb (direct obj)
辿り着く,たどりつく – to grope along to, to struggle on to, to arrive somewhere after a struggle
辿る,たどる – to follow (road), to pursue (course), to follow up
掌,たなごころ – the palm
楽しむ,たのしむ – to enjoy oneself
頼み,たのみ – request, favor, reliance, dependence
煙草,たばこ – (pt:) (n) (uk) tobacco (pt: tabaco), cigarettes
度々,たびたび – often, repeatedly, frequently
他方,たほう – another side, different direction, (on) the other hand
多忙,たぼう – busy, pressure of work
給う,たまう – to receive, to grant
偶に,たまに – occasionally, once in a while
堪らない,たまらない – intolerable, unbearable, unendurable
溜まり,たまり – collected things, gathering place, arrears
賜る,たまわる – to grant, to bestow
例,ためし – instance, example, case, precedent, experience, custom, usage, parallel, illustration
躊躇う,ためらう – to hesitate
保つ,たもつ – to keep, to preserve, to hold, to retain, to maintain, to support, to sustain, to last, to endure, to keep we
容易い,たやすい – easy, simple, light
多様,たよう – diversity, variety
弛み,たるみ – slack, slackening, dullness, letdown
弛む,たるむ – to slacken, to loosen, to relax
誰,たれ – adjectival suffix for a person
垂れる,たれる – to hang, to droop, to drop, to lower, to pull down, to dangle, to sag, to drip, to ooze, to trickle, to leave
歎,たん – grief, sigh, lamentation
反,たん – roll of cloth (c. 10 yds.), .245 acres, 300 tsubo
単一,たんいつ – single, simple, sole, individual, unitory
短歌,たんか – tanka, 31-syllable Japanese poem
担架,たんか – stretcher, litter
短気,たんき – quick temper
探検,たんけん – exploration, expedition
短縮,たんしゅく – shortening, abbreviation, reduction
箪笥,たんす – chest of drawers
炭素,たんそ – carbon (C)
短大,たんだい – junior college
単調,たんちょう – monotony, monotone, dullness
単独,たんどく – sole, independence, single, solo (flight)
短波,たんぱ – short wave
蛋白質,たんぱくしつ – protein
第,だい – ordinal
第一,だいいち – first, foremost, # 1
大胆,だいたん – bold, daring, audacious
台無し,だいなし – mess, spoiled, (come to) nothing
大便,だいべん – feces, excrement, shit
代弁,だいべん – pay by proxy, act for another, speak for another
台本,だいほん – libretto, scenario
代用,だいよう – substitution
打開,だかい – break in the deadlock
妥協,だきょう – compromise, giving in
丈,だけ – only, just, as
妥結,だけつ – agreement
打撃,だげき – 1. blow, shock, strike, damage, 2. batting (baseball)
駄作,ださく – poor work, rubbish
脱出,だっしゅつ – escape
脱する,だっする – to escape from, to get out
脱退,だったい – secession
,だぶだぶ – loose, baggy
騙す,だます – to trick, to cheat, to deceive
,だらけ – implying (negatively) that something is full of e.g. mistakes
怠い,だるい – sluggish, feel heavy, languid, dull
壇,だん – 1. platform, podium, rostrum, 2. (arch) mandala
団結,だんけつ – unity, union, combination
断言,だんげん – declaration, affirmation
断然,だんぜん – firmly, absolutely, definitely
段々,だんだん – gradually, by degrees
旦那,だんな – master (of house), husband (informal)
断面,だんめん – cross section
弾力,だんりょく – elasticity, flexibility
治安,ちあん – public order
近付く,ちかづく – to approach, to get near, to get acquainted with, to get closer
違える,ちがえる – to change
契る,ちぎる – to pledge, to promise, to swear
畜産,ちくさん – animal husbandry
畜生,ちくしょう – beast, brute, damn
蓄積,ちくせき – accumulation, accumulate, store
知性,ちせい – intelligence
乳,ちち – milk, breast, loop
父母,ちちはは – father and mother, parents
縮まる,ちぢまる – to be shortened, to be contracted, to shrink
窒息,ちっそく – suffocation
些とも,ちっとも – not at all (neg. verb)
秩序,ちつじょ – order, regularity, system, method
知的,ちてき – intellectual
著,ちゃく – counter for suits of clothing, arriving at ..
着,ちゃく – counter for suits of clothing, arriving at ..
着手,ちゃくしゅ – embarkation, launch
着色,ちゃくしょく – colouring, coloring
着席,ちゃくせき – sit down, seat
着目,ちゃくもく – attention
着陸,ちゃくりく – landing, alighting, touch down
着工,ちゃっこう – start of (construction) work
茶の間,ちゃのま – living room (Japanese style)
茶の湯,ちゃのゆ – tea ceremony
,ちやほや – pamper, make a fuss of, spoil
昼間,ちゅうかん – daytime, during the day
宙返り,ちゅうがえり – somersault, looping-the-loop
中継,ちゅうけい – relay, hook-up
忠告,ちゅうこく – advice, warning
中指,ちゅうし – middle finger
中傷,ちゅうしょう – slander, libel, defamation
忠実,ちゅうじつ – fidelity, faithfulness
中枢,ちゅうすう – centre, pivot, mainstay, nucleus, backbone, central figure, pillar, key man
抽選,ちゅうせん – lottery, raffle, drawing (of lots)
中断,ちゅうだん – interruption, suspension, break
中腹,ちゅうっぱら – irritated, offended
中毒,ちゅうどく – poisoning
仲人,ちゅうにん – go-between, matchmaker
昼飯,ちゅうはん – lunch, midday meal
中立,ちゅうりつ – neutrality
中和,ちゅうわ – neutralize, counteract
腸,ちょう – guts, bowels, intestines
蝶,ちょう – butterfly
超,ちょう – super-, ultra-, hyper-
庁,ちょう – government office
調印,ちょういん – signature, sign, sealing
聴覚,ちょうかく – the sense of hearing
長官,ちょうかん – chief, (government) secretary
聴講,ちょうこう – lecture attendance, auditing
徴収,ちょうしゅう – collection, levy
聴診器,ちょうしんき – stethoscope
挑戦,ちょうせん – challenge, defiance
長大,ちょうだい – very long, great length
調停,ちょうてい – arbitration, conciliation, mediation
恰度,ちょうど – just, right, exactly
長編,ちょうへん – long (e.g. novel film)
丁目,ちょうめ – district of a town, city block (of irregular size)
調理,ちょうり – cooking
調和,ちょうわ – harmony
,ちょくちょく – often, frequently, now and then, occasionally
直面,ちょくめん – confrontation
著書,ちょしょ – literary work, book
貯蓄,ちょちく – savings
直感,ちょっかん – intuition
一寸,ちょっと – (ateji) (adv int) (uk) just a minute, a short time, a while, just a little, somewhat, easily, readily, rath
著名,ちょめい – well-known, noted, celebrated
,ちらっと – at a glance, by accident
塵取り,ちりとり – dustpan
治療,ちりょう – medical treatment
賃金,ちんぎん – wages
沈殿,ちんでん – precipitation, settlement
沈没,ちんぼつ – sinking, foundering
沈黙,ちんもく – silence, reticence
陳列,ちんれつ – exhibition, display, show
追及,ついきゅう – gaining on, carrying out, solving (crime)
追跡,ついせき – pursuit
次いで,ついで – next, secondly, subsequently
追放,ついほう – exile, banishment
費やす,ついやす – to spend, to devote, to waste
墜落,ついらく – falling, crashing
通,つう – connoisseur, counter for letters
痛感,つうかん – feeling keenly, fully realizing
通常,つうじょう – common, general, usually
痛切,つうせつ – keen, acute
杖,つえ – cane
遣い,つかい – mission, simple task, doing
使い道,つかいみち – use
仕える,つかえる – to serve, to work for
司る,つかさどる – to rule, to govern, to administer
束の間,つかのま – moment, brief time, brief, transient
付き,つき – attached to, impression, sociality, appearance, furnished with, under, to
付き合う,つきあう – to associate with, to keep company with, to get on with
月並み,つきなみ – every month, common
尽きる,つきる – to be used up, to be run out, to be exhausted, to be consumed, to come to an end
継ぎ目,つぎめ – a joint, joining point
吐く,つく – 1. to breathe, 2. to tell (lies), 3. to vomit, to disgorge
尽くす,つくす – to exhaust, to run out, to serve (a person), to befriend
作り,つくり – make-up, sliced raw fish
造り,つくり – make up, structure, physique
造る,つくる – to make, to create, to manufacture, to draw up, to write, to compose, to build, to coin, to cultivate, to org
繕う,つくろう – to mend, to repair, to fix, to patch up, to darn, to tidy up, to adjust, to trim
接ぐ,つぐ – to join, to piece together, to set (bones), to graft (trees)
継ぐ,つぐ – to succeed
付け加える,つけくわえる – to add one thing to another
告げる,つげる – to inform
辻褄,つじつま – coherence, consistency
途中,つちゅう – on the way, en route
突っ張る,つっぱる – to support, to become stiff, to become taut, to thrust (ones opponent), to stick to (ones opinion), to in
筒,つつ – pipe, tube
銃,つつ – gun
突く,つつく – 1. to thrust, to strike, to attack, 2. to poke, to nudge, to pick at
慎む,つつしむ – to be careful, to be chaste or discreet, to abstain or refrain
伝言,つてごと – verbal message, rumor, word
勤まる,つとまる – to be fit for, to be equal to, to function properly
勤め先,つとめさき – place of work
努めて,つとめて – make an effort!, work hard!
津波,つなみ – tsunami, tidal wave
抓る,つねる – to pinch
募る,つのる – to invite, to solicit help participation etc
唾,つば – saliva, sputum
呟く,つぶやく – to mutter, to murmur
瞑る,つぶる – to close the eyes
壷,つぼ – tsubo jar, pot, vase
蕾,つぼみ – bud, flower bud
躓く,つまずく – to stumble, to trip
摘む,つまむ – to pinch, to hold, to pick up
詰らない,つまらない – insignificant, boring, trifling
詰まり,つまり – in short, in brief, in other words, that is to say, in the long run, after all, blockade, stuffing, ultimate
積もり,つもり – intention, plan
露,つゆ – dew
強まる,つよまる – to get strong, to gain strength
強める,つよめる – to strengthen, to emphasize
連なる,つらなる – to extend, to stretch out, to stand in a row
貫く,つらぬく – to go through
連ねる,つらねる – to link, to join, to put together
釣り,つり – fishing, angling
吊り革,つりかわ – strap
釣鐘,つりがね – hanging bell
吊るす,つるす – to hang
手当て,てあて – allowance, compensation, treatment, medical care
体,てい – appearance, air, condition, state, form
提供,ていきょう – offer, tender, program sponsoring, furnishing
定義,ていぎ – definition
提携,ていけい – cooperation, tie-up, joint business, link-up
体裁,ていさい – decency, style, form, appearance, show, get-up, format
梯子,ていし – ladder, stairs
定食,ていしょく – set meal, special (of the day)
提示,ていじ – presentation, exhibit, suggest, citation
訂正,ていせい – correction, revision
停滞,ていたい – stagnation, tie-up, congestion, retention, accumulation, falling into arrears
邸宅,ていたく – mansion, residence
定年,ていねん – retirement age
堤防,ていぼう – bank, weir
手遅れ,ておくれ – too late, belated treatment
手数,てかず – number of moves, trouble
手掛かり,てがかり – contact, trail, scent, on hand, hand hold, clue, key
手掛ける,てがける – to handle, to manage, to work with, to rear, to look after, to have experience with
手軽,てがる – easy, simple, informal, offhand, cheap
的,てき – -like, typical
適応,てきおう – adaptation, accommodation, conformity
適宜,てきぎ – suitability
適性,てきせい – aptitude
手際,てぎわ – performance, skill, tact
手順,てじゅん – process, procedure, protocol
手錠,てじょう – handcuffs, manacles
手近,てぢか – near, handy, familiar
,てっきり – surely, certainly, beyond doubt
鉄鋼,てっこう – iron and steel
徹する,てっする – to sink in, to penetrate, to devote oneself, to believe in, to go through, to do intently and exclusively
鉄片,てっぺん – iron scraps
手配,てはい – arrangement, search (by police)
手筈,てはず – arrangement, plan, programme
手引き,てびき – guidance, guide, introduction
手本,てほん – model, pattern
手回し,てまわし – preparations, arrangements
手元,てもと – on hand, at hand, at home
照り返す,てりかえす – to reflect, to throw back light
手分け,てわけ – division of labour
店,てん – store, shop, establishment
点火,てんか – ignition, lighting, set fire to
転回,てんかい – revolution, rotation
転換,てんかん – convert, divert
転居,てんきょ – moving, changing residence
転勤,てんきん – transfer, transmission
点検,てんけん – inspection, examination, checking
転校,てんこう – change schools
天国,てんごく – paradise, heaven, Kingdom of Heaven
天才,てんさい – genius, prodigy, natural gift
天災,てんさい – natural calamity, disaster
展示,てんじ – exhibition, display
天井,てんじょう – ceiling, ceiling price
転じる,てんじる – to turn, to shift, to alter, to distract
点線,てんせん – dotted line, perforated line
天体,てんたい – heavenly body
転転,てんてん – rolling about, moving from place to place, being passed around repeatedly
,てんで – (not) at all, altogether, entirely
転任,てんにん – change of post
展望,てんぼう – view, outlook, prospect
転落,てんらく – fall, degradation, slump
出合う,であう – to meet by chance, to come across, to happen to encounter, to hold a rendezvous, to have a date
出入り口,でいりぐち – exit and entrance
,でかい – huge
出来物,できもの – able man, tumour, growth, boil, ulcer, abcess, rash, pimple
出切る,できる – to be out of, to have no more at hand
出くわす,でくわす – to happen to meet, to come across
出鱈目,でたらめ – irresponsible utterance, nonsense, nonsensical, random, haphazard, unsystematic
出直し,でなおし – adjustment, touch up
田園,でんえん – country, rural districts
電源,でんげん – source of electricity, power (button on TV etc.)
伝説,でんせつ – tradition, legend, folklore
電線,でんせん – electric line
伝達,でんたつ – transmission (e.g. news), communication, delivery
伝来,でんらい – ancestral, hereditary, imported, transmitted, handed down
,と – 1. if (conjunction), 2. promoted pawn (shogi) (abbr)
問い合わせる,といあわせる – to enquire, to seek information
問屋,といや – wholesale store
問う,とう – to ask, to question, to charge (i.e. with a crime), to accuse, without regard to (neg)
棟,とう – place, section, building
等,とう – et cetera, etc., and the like
陶器,とうき – pottery, ceramics
等級,とうきゅう – grade, class
討議,とうぎ – debate, discussion
登校,とうこう – attendance (at school)
統合,とうごう – integration, unification, synthesis
倒産,とうさん – (corporate) bankruptcy, insolvency
投資,とうし – investment
統治,とうじ – rule, reign, government, governing
統制,とうせい – regulation, control
当選,とうせん – being elected, winning the prize
逃走,とうそう – flight, desertion, escape
統率,とうそつ – command, lead, generalship, leadership
到達,とうたつ – reaching, attaining, arrival
到底,とうてい – (cannot) possibly
丁々,とうとう – clashing of swords, felling of trees, ringing of an ax
投入,とうにゅう – throw, investment, making (an electrical circuit)
当人,とうにん – the one concerned, the said person
逃亡,とうぼう – escape
冬眠,とうみん – hibernation, winter sleep
登録,とうろく – registration, register, entry, record
討論,とうろん – debate, discussion
遠ざかる,とおざかる – to go far off
遠回り,とおまわり – detour, roundabout way
通りかかる,とおりかかる – to happen to pass by
兎角,とかく – anyhow, anyway, somehow or other, generally speaking, in any case, this and that, many, be apt to
咎める,とがめる – to blame, to find fault, to take someone to task, to aggravate (an injury)
時折,ときおり – sometimes
跡切れる,とぎれる – to pause, to be interrupted
説く,とく – to explain, to advocate, to preach, to persuade
特技,とくぎ – special skill
特産,とくさん – specialty, special product
特集,とくしゅう – feature (e.g. newspaper), special edition, report
得点,とくてん – score, points made, marks obtained, runs
特派,とくは – send specially, special envoy
特有,とくゆう – characteristic (of), peculiar (to)
研ぐ,とぐ – to sharpen, to grind, to scour, to hone, to polish, to wash (rice)
刺,とげ – thorn, splinter, spine, biting words
遂げる,とげる – to accomplish, to achieve, to carry out
床,とこ – bed, sickbed, alcove, padding
所が,ところが – however, while, even if
所で,ところで – by the way, even if, no matter what
年頃,としごろ – age, marriageable age, age of puberty, adolescence, for some years
年寄り,としより – old people, the aged
戸締り,とじまり – closing up, fastening the doors
途上,とじょう – en route, half way
綴じる,とじる – to bind, to file
途絶える,とだえる – to stop, to cease, to come to an end
特許,とっきょ – special permission, patent
疾っくに,とっくに – long ago, already, a long time ago
特権,とっけん – privilege, special right
咄嗟,とっさ – moment, instant
取っ手,とって – handle, grip, knob
突破,とっぱ – breaking through, breakthrough, penetration
突如,とつじょ – suddenly, all of a sudden
迚も,とても – very, awfully, exceedingly
整える,ととのえる – to put in order, to get ready, to arrange, to adjust
届け,とどけ – report, notification, registration
滞る,とどこおる – to stagnate, to be delayed
止まる,とどまる – to be limited to
留める,とどめる – to stop, to cease, to put an end to
止める,とどめる – to stop, to cease, to put an end to
唱える,となえる – to recite, to chant, to call upon
兎に角,とにかく – anyhow, at any rate, anyway, somehow or other, generally speaking, in any case
殿様,とのさま – feudal lord
幕,とばり – curtain, bunting, act (in play)
帳,とばり – curtain
扉,とびら – door, opening
徒歩,とほ – walking, going on foot
乏しい,とぼしい – meagre, scarce, limited, destitute, hard up, scanty, poor
富,とみ – wealth, fortune
富む,とむ – to be rich, to become rich
兎も角,ともかく – anyhow, anyway, somehow or other, generally speaking, in any case
共稼ぎ,ともかせぎ – working together, (husband and wife) earning a living together
灯,ともしび – light
伴う,ともなう – to accompany, to bring with, to be accompanied by, to be involved in
共働き,ともばたらき – dual income
捕らえる,とらえる – to seize, to grasp, to capture, to arrest
取りあえず,とりあえず – at once, first of all, for the time being
取り扱い,とりあつかい – treatment, service, handling, management
取り扱う,とりあつかう – to treat, to handle, to deal in
鳥居,とりい – torii (Shinto shrine archway)
取り替え,とりかえ – swap, exchange
取り組む,とりくむ – to tackle, to wrestle with, to engage in a bout, to come to grips with
取り締まり,とりしまり – control, management, supervision
取り締まる,とりしまる – to manage, to control, to supervise
取り調べる,とりしらべる – to investigate, to examine
取り立てる,とりたてる – to collect, to extort, to appoint, to promote
取り次ぐ,とりつぐ – to act as an agent for, to announce (someone), to convey (a message)
取り除く,とりのぞく – to remove, to take away, to set apart
取り引き,とりひき – transactions, dealings, business
取り巻く,とりまく – to surround, to circle, to enclose
取り混ぜる,とりまぜる – to mix, to put together
取り戻す,とりもどす – to take back, to regain
取り寄せる,とりよせる – to order, to send away for
取り分,とりわけ – especially, above all
副,とりわけ – especially, above all
蕩ける,とろける – to be enchanted with
,とんだ – terrible, awful, serious, preposterous, absolutely not
胴,どう – trunk, body, frame
働,どう – work, labor
同,どう – the same, the said, ibid.
同意,どうい – agreement, consent, same meaning, same opinion, approval
動員,どういん – mobilization
同感,どうかん – agreement, same opinion, same feeling, sympathy, concurrence
動機,どうき – motive, incentive
同級,どうきゅう – the same grade, same class
同居,どうきょ – living together
動向,どうこう – trend, tendency, movement, attitude
同士,どうし – fellow, companion, comrade
同志,どうし – same mind, comrade, kindred soul
如何して,どうして – why?, for what reason, how, in what way, for what purpose, what for
如何しても,どうしても – by all means, at any cost, no matter what, after all, in the long run, cravingly, at any rate, surely
同情,どうじょう – sympathy, compassion, sympathize, pity, feel for
道場,どうじょう – dojo, hall used for martial arts training, mandala
何卒,どうぞ – please, kindly, by all means
どうぞ宜しく,どうぞよろしく – pleased to meet you
同調,どうちょう – sympathy, agree with, alignment, tuning
動的,どうてき – dynamic, kinetic
同等,どうとう – equality, equal, same rights, same rank
堂々,どうどう – magnificent, grand, impressive
,どうにか – in some way or other, one way or another
導入,どうにゅう – introduction, bringing in, leading in
同封,どうふう – enclosure (e.g. in a letter)
同盟,どうめい – alliance, union, league
,どうやら – it seems like, somehow or other
動揺,どうよう – disturbance, unrest, shaking, trembling, pitching, rolling, oscillation, agitation, excitement, commotion
動力,どうりょく – power, motive power, dynamic force
独裁,どくさい – dictatorship, despotism
読者,どくしゃ – reader
独自,どくじ – original, peculiar, characteristic
独占,どくせん – monopoly
独創,どくそう – originality
何処,どこ – where, what place
何処か,どこか – somewhere, anywhere, in some respects
土産,どさん – product of the land
土台,どだい – foundation, base, basis
何方,どちら – which, who
土手,どて – embankment, bank
何方,どなた – who?
怒鳴る,どなる – to shout, to yell
何の,どの – which, what
土俵,どひょう – arena
土木,どぼく – public works
何れ,どれ – well, now, let me see, which (of three or more)
何々,どれどれ – which (emphatic)
度忘れ,どわすれ – lapse of memory, forget for a moment
鈍感,どんかん – thickheadedness, stolidity
内閣,ないかく – cabinet, (government) ministry
乃至,ないし – from...to, between...and, or
内臓,ないぞう – internal organs, intestines, viscera
内部,ないぶ – interior, inside, internal
内乱,ないらん – civil war, insurrection, rebellion, domestic conflict
内陸,ないりく – inland
苗,なえ – rice seedling
尚,なお – furthermore, still, yet, more, still more, greater, further, less
尚更,なおさら – all the more, still less
中程,なかほど – middle, midway
流し,ながし – sink
長々,ながなが – long, drawn-out, very long
殴る,なぐる – to strike, to hit
嘆く,なげく – to sigh, to lament, to grieve
投げ出す,なげだす – to throw down, to abandon, to sacrifice, to throw out
和やか,なごやか – mild, calm, gentle, quiet, harmonious
名残,なごり – remains, traces, memory
情け,なさけ – sympathy, compassion
情け深い,なさけぶかい – tender-hearted, compassionate
為さる,なさる – to do
詰る,なじる – to rebuke, to scold, to tell off
何故,なぜ – why, how
何故なら,なぜなら – because
名高い,なだかい – famous, celebrated, well-known
雪崩,なだれ – avalanche
懐く,なつく – to become emotionally attached
名付ける,なづける – to name (someone)
何気ない,なにげない – casual, unconcerned
何しろ,なにしろ – at any rate, anyhow, anyway, in any case
何卒,なにとぞ – please
何も,なにも – nothing
何より,なにより – most, best
七日,なぬか – seven days, the seventh day (of the month)
名札,なふだ – name plate, name tag
生臭い,なまぐさい – smelling of fish or blood, fish or meat
生温い,なまぬるい – lukewarm, halfhearted
生身,なまみ – living flesh, flesh and blood, the quick
鉛,なまり – lead (the metal)
鈍る,なまる – to become less capable, to grow dull, to become blunt, to weaken
並み,なみ – average, medium, common, ordinary
滑らか,なめらか – smoothness, glassiness
嘗める,なめる – to lick, to taste, to experience, to make fun of, to make light of, to put down, to treat with contempt
悩ましい,なやましい – seductive, melancholy, languid
悩ます,なやます – to afflict, to torment, to harass, to molest
悩み,なやみ – trouble(s), worry, distress, anguish, agony, problem
平均,ならし – equilibrium, balance, average, mean
慣らす,ならす – to accustom
馴らす,ならす – to domesticate, to tame
並びに,ならびに – and
成り立つ,なりたつ – to conclude, to consist of, to be practical (logical feasible viable), to hold true
成る丈,なるたけ – as much as possible, if possible
成るべく,なるべく – as much as possible
慣れ,なれ – practice, experience
馴れ馴れしい,なれなれしい – over-familiar
難,なん – difficulty, hardships, defect
南,なん – south
,なんか – things like ..., or something like that .. (often derogatory)
何だか,なんだか – a little, somewhat, somehow
,なんだかんだ – something or other
何て,なんて – how...!, what...!
何と,なんと – what, how, whatever
何となく,なんとなく – somehow or other, for some reason or another
何とも,なんとも – nothing (with neg. verb), quite, not a bit
何なり,なんなり – any, anything, whatever
荷,に – load, baggage, cargo
似通う,にかよう – to resemble closely
面皰,にきび – pimple, acne
賑わう,にぎわう – to prosper, to flourish, to do thriving business, to be crowded with people
悪い,にくい – hateful, abominable, poor-looking
憎しみ,にくしみ – hatred
肉親,にくしん – blood relationship, blood relative
肉体,にくたい – the body, the flesh
逃げ出す,にげだす – to run away, to escape from
西日,にしび – westering sun
滲む,にじむ – to run, to blur, to spread, to blot, to ooze
日夜,にちや – day and night, always
日当,にっとう – daily allowance
荷造り,にづくり – packing, baling, crating
担う,になう – to carry on shoulder, to bear (burden), to shoulder (gun)
二人,ににん – two persons, two people, pair, couple
にも拘らず,にもかかわらず – in spite of, nevertheless
入手,にゅうしゅ – obtaining, coming to hand
入賞,にゅうしょう – winning a prize or place (in a contest)
入浴,にゅうよく – bathe, bathing
尿,にょう – urine
俄か,にわか – sudden, abrupt, unexpected, improvised, offhand
認識,にんしき – recognition, cognizance
妊娠,にんしん – conception, pregnancy
人情,にんじょう – humanity, empathy, kindness, sympathy, human nature, common sense, customs and manners
任務,にんむ – duty, function, office, mission, task
任命,にんめい – appointment, nomination, ordination, commission, designation
抜かす,ぬかす – to omit, to leave out
抜け出す,ぬけだす – to slip out, to sneak away, to excel
盗み,ぬすみ – stealing
沼,ぬま – swamp, bog, pond, lake
音,ね – sound, note
値打ち,ねうち – value, worth, price, dignity
寝かせる,ねかせる – to put to bed, to lay down, to ferment
捻子,ねじ – screw, helix, spiral
ねじ回し,ねじまわし – screwdriver
捻じれる,ねじれる – to twist, to wrench, to screw
鼠,ねず – 1. mouse, rat, 2. dark gray, slate color
妬む,ねたむ – to be jealous, to be envious
強請る,ねだる – to tease, to coax, to solicit, to demand
熱湯,ねっとう – boiling water
熱意,ねつい – zeal, enthusiasm
熱量,ねつりょう – temperature
粘り,ねばり – stickyness, viscosity
粘る,ねばる – to be sticky, to be adhesive, to persevere, to persist, to stick to
値引き,ねびき – price reduction, discount
根回し,ねまわし – making necessary arrangements
眠たい,ねむたい – sleepy
練る,ねる – to knead, to work over, to polish up
念,ねん – sense, idea, thought, feeling, desire, concern, attention, care
年鑑,ねんかん – yearbook
年号,ねんごう – name of an era, year number
燃焼,ねんしょう – burning, combustion
年生,ねんせい – pupil in .... year, student in .... year
年長,ねんちょう – seniority
燃料,ねんりょう – fuel
年輪,ねんりん – annual tree ring
脳,のう – brain, memory
農耕,のうこう – farming, agriculture
農場,のうじょう – farm (agriculture)
農地,のうち – agricultural land
納入,のうにゅう – payment, supply
逃す,のがす – to let loose, to set free, to let escape
逃れる,のがれる – to escape
軒並み,のきなみ – row of houses
鋸,のこぎり – saw
望ましい,のぞましい – desirable, hoped for
臨む,のぞむ – to look out on, to face, to deal with, to attend (function)
乗っ取る,のっとる – to capture, to occupy, to usurp
長閑,のどか – tranquil, calm, quiet
罵る,ののしる – to speak ill of, to abuse
延べ,のべ – futures, credit (buying), stretching, total
飲み込む,のみこむ – to gulp down, to swallow deeply, to understand, to take in, to catch on to, to learn, to digest
乗り換え,のりかえ – transfer (trains buses etc.)
乗り込む,のりこむ – to board, to embark on, to get into (a car), to ship (passengers), to man (a ship), to help (someone) int
刃,は – edge (of a sword)
派,は – clique, faction, school
把握,はあく – grasp, catch, understanding
肺,はい – lung
廃棄,はいき – annullment, disposal, abandon, scrap, discarding, repeal
配給,はいきゅう – distribution (eg. films rice)
配偶者,はいぐうしゃ – spouse, wife, husband
拝啓,はいけい – Dear (so and so)
背景,はいけい – background, scenery, setting, circumstance
背後,はいご – back, rear
灰皿,はいさら – ashtray
廃止,はいし – abolition, repeal
拝借,はいしゃく – borrowing
排除,はいじょ – exclusion, removal, rejection
排水,はいすい – drainage
敗戦,はいせん – defeat, losing a war
配置,はいち – arrangement (of resources), disposition
配布,はいふ – distribution
配分,はいぶん – distribution, allotment
配慮,はいりょ – consideration, concern, forethought
配列,はいれつ – arrangement, array (programming)
映える,はえる – to shine, to look attractive, to look pretty
破壊,はかい – destruction
墓地,はかち – cemetery, graveyard
捗る,はかどる – to make progress, to move right ahead (with the work), to advance
果ない,はかない – fleeting, transient, short-lived, momentary, vain, fickle, miserable, empty, ephemeral
諮る,はかる – to consult with, to confer
図る,はかる – to plot, to attempt, to plan, to take in, to deceive, to devise, to design, to refer A to B
剥がす,はがす – to tear off, to peel off, to rip off, to strip off, to skin, to flay, to disrobe, to deprive of, to detach, t
破棄,はき – revocation, annulment, breaking (e.g. treaty)
泊,はく – counter for nights of a stay
迫害,はくがい – persecution
薄弱,はくじゃく – feebleness, weakness, weak
白状,はくじょう – confession
剥ぐ,はぐ – to tear off, to peel off, to rip off, to strip off, to skin, to flay, to disrobe, to deprive of
派遣,はけん – dispatch, send
励ます,はげます – to encourage, to cheer, to raise (the voice)
励む,はげむ – to be zealous, to brace oneself, to endeavour, to strive, to make an effort
剥げる,はげる – to come off, to be worn off, to fade, to discolor
鋏,はさみ – scissors
柱,はしら – pillar, post
橋渡し,はしわたし – bridge building, mediation
恥,はじ – shame, embarrassment
弾く,はじく – to flip, to snap
始め,はじめ – beginning, start, origin
始めまして,はじめまして – How do you do?, I am glad to meet you
恥じらう,はじらう – to feel shy, to be bashful, to blush
恥じる,はじる – to feel ashamed
蓮,はす – lotus
筈,はず – it should be so
弾む,はずむ – to spring, to bound, to bounce, to be stimulated, to be encouraged, to get lively, to treat oneself to, to
破損,はそん – damage
機,はた – loom
果たして,はたして – as was expected, really
果たす,はたす – to accomplish, to fulfill, to carry out, to achieve
裸足,はだし – barefoot
蜂蜜,はちみつ – honey
発掘,はっくつ – excavation, exhumation
発生,はっせい – outbreak, spring forth, occurrence, incidence, origin
発足,はっそく – starting, inauguration
初,はつ – first, new
発,はつ – departure, beginning, counter for gunshots
発育,はついく – (physical) growth, development
発芽,はつが – burgeoning
発言,はつげん – utterance, speech, proposal
発病,はつびょう – attack (disease)
初耳,はつみみ – something heard for the first time
果て,はて – the end, the extremity, the limit(s), the result
果てる,はてる – to end, to be finished, to be exhausted, to die, to perish
話し合い,はなしあい – discussion, conference
甚だ,はなはだ – very, greatly, exceedingly
華々しい,はなばなしい – brilliant, magnificent, spectacular
花びら,はなびら – (flower) petal
華やか,はなやか – gay, showy, brilliant, gorgeous, florid
阻む,はばむ – to keep someone from doing, to stop, to prevent, to check, to hinder, to obstruct, to oppose, to thwart
浜,はま – beach, seashore
浜辺,はまべ – beach, foreshore
填まる,はまる – to get into, to go into, to fit, to be fit for, to suit, to fall into, to plunge into, to be deceived, to be
歯磨,はみがき – dentifrice, toothpaste
填める,はめる – to get in, to insert, to put on, to make love
生やす,はやす – to grow, to cultivate, to wear beard
早める,はやめる – to hasten, to quicken, to expedite, to precipitate, to accelerate
流行,はやり – fashionable, fad, in vogue, prevailing
腹立ち,はらだち – anger
原っぱ,はらっぱ – open field, empty lot, plain
張り紙,はりがみ – paper patch, paper backing, poster
遥か,はるか – far, far-away, distant, remote, far off
破裂,はれつ – explosion, rupture, break off
腫れる,はれる – to swell (from inflammation), to become swollen
班,はん – group, party, section (mil)
判,はん – seal, stamp, monogram signature, judgment
版,はん – edition
繁栄,はんえい – prospering, prosperity, thriving, flourishing
反感,はんかん – antipathy, revolt, animosity
版画,はんが – art print
反響,はんきょう – echo, reverberation, repercussion, reaction, influence
判決,はんけつ – judicial decision, judgement, sentence, decree
反撃,はんげき – counterattack, counteroffensive, counterblow
反射,はんしゃ – reflection, reverberation
繁殖,はんしょく – breed, multiply, increase, propagation
繁盛,はんじょう – prosperity, flourishing, thriving
反する,はんする – to be inconsistent with, to oppose, to contradict, to transgress, to rebel
判定,はんてい – judgement, decision, award, verdict
反応,はんのう – reaction, response
半端,はんぱ – remnant, fragment, incomplete set, fraction, odd sum, incompleteness
反発,はんぱつ – repelling, rebound, recover, oppose
反乱,はんらん – insurrection, mutiny, rebellion, revolt, uprising
氾濫,はんらん – overflowing, flood
黴菌,ばいきん – bacteria, germ(s)
賠償,ばいしょう – reparations, indemnity, compensation
倍率,ばいりつ – diameter, magnification
馬鹿馬鹿しい,ばかばかしい – stupid
馬鹿らしい,ばからしい – absurd
漠然,ばくぜん – obscure, vague, equivocal
爆弾,ばくだん – bomb
爆破,ばくは – blast, explosion, blow up
暴露,ばくろ – disclosure, exposure, revelation
化ける,ばける – to appear in disguise, to take the form of, to change for the worse
罰,ばち – (divine) punishment, curse, retribution
伐,ばつ – strike, attack, punish
,ばてる – to be exhausted, to be worn out
発条,ばね – spring (e.g. coil leaf)
散蒔く,ばらまく – to disseminate, to scatter, to give money freely
判,ばん – size (of paper or books)
万,ばん – many, all
万人,ばんじん – all people, everybody, 10000 people
万能,ばんのう – all-purpose, almighty, omnipotent
番目,ばんめ – cardinal number suffix
非,ひ – faulty-, non-
費,ひ – cost, expense
延いては,ひいては – not only...but also, in addition to, consequently
控室,ひかえしつ – waiting room
控える,ひかえる – to draw in, to hold back, to make notes, to be temperate in
悲観,ひかん – pessimism, disappointment
匹,ひき – head, small animal counter, roll of cloth
引き上げる,ひきあげる – to withdraw, to leave, to pull out, to retire
率いる,ひきいる – to lead, to spearhead (a group), to command (troops)
引き受ける,ひきうける – to undertake, to take up, to take over, to be responsible for, to guarantee, to contract (disease)
引き起こす,ひきおこす – to cause
引き下げる,ひきさげる – to pull down, to lower, to reduce, to withdraw
引きずる,ひきずる – to seduce, to drag along, to pull, to prolong, to support
引き取る,ひきとる – to take charge of, to take over, to retire to a private place
引き分け,ひきわけ – a draw (in competition), tie game
否決,ひけつ – rejection, negation, voting down
非行,ひこう – delinquency, misconduct
日頃,ひごろ – normally, habitually
久しい,ひさしい – long, long-continued, old (story)
久し振り,ひさしぶり – after a long time
悲惨,ひさん – misery
秘書,ひしょ – (private) secretary
比重,ひじゅう – specific gravity
密か,ひそか – secret, private, surreptitious
浸す,ひたす – to soak, to dip, to drench
一向,ひたすら – earnestly
左利き,ひだりきき – left-handedness, sake drinker, left-hander
引っ掻く,ひっかく – to scratch
引っ掛ける,ひっかける – 1. to hang (something) on (something), to throw on (clothes), 2. to hook, to catch, to trap, to ensnar
必修,ひっしゅう – required (subject)
匹敵,ひってき – comparing with, match, rival, equal
未,ひつじ – eighth sign of Chinese zodiac (The Ram 1pm-3pm south-southwest June)
必然,ひつぜん – inevitable, necessary
一息,ひといき – puffy, a breath, a pause, an effort
単,ひとえ – one layer, single
人柄,ひとがら – personality, character, personal appearance, gentility
一頃,ひところ – once, some time ago
人質,ひとじち – hostage, prisoner
一筋,ひとすき – a line, earnestly, blindly, straightforwardly
一まず,ひとまず – for the present, once, in outline
一人でに,ひとりでに – by itself, automatically, naturally
酷い,ひどい – cruel, awful, severe, very bad, serious, terrible, heavy, violent
日取り,ひどり – fixed date, appointed day
雛,ひな – young bird, chick, doll
日向,ひなた – sunny place, in the sun
非難,ひなん – blame, attack, criticism
避難,ひなん – taking refuge, finding shelter
日の丸,ひのまる – the Japanese flag
火花,ひばな – spark
日々,ひび – every day, daily, day after day
悲鳴,ひめい – shriek, scream
百科事典,ひゃっかじてん – encyclopedia
百科辞典,ひゃっかじてん – encyclopedia
冷やかす,ひやかす – to banter, to make fun of, to jeer at, to cool, to refrigerate
日焼け,ひやけ – sunburn
票,ひょう – label, ballot, ticket, sign
標語,ひょうご – motto, slogan, catchword
,ひょっと – possibly, accidentally
平たい,ひらたい – flat, even, level, simple, plain
比率,ひりつ – ratio, proportion, percentage
肥料,ひりょう – manure, fertilizer
比例,ひれい – proportion
疲労,ひろう – fatigue, weariness
広まる,ひろまる – to spread, to be propagated
貧困,ひんこん – poverty, lack
品質,ひんしつ – quality
品種,ひんしゅ – brand, kind, description
貧弱,ひんじゃく – poor, meagre, insubstantial
頻繁,ひんぱん – frequency
美,び – beauty
微笑,びしょう – smile
美術,びじゅつ – art, fine arts
吃驚,びっくり – be surprised, be amazed, be frightened, astonishment
,びっしょり – wet through, drenched
描写,びょうしゃ – depiction, description, portrayal
,びり – last on the list, at the bottom
微量,びりょう – minuscule amount, extremely small quantity
敏感,びんかん – sensibility, susceptibility, sensitive (to), well attuned to
貧乏,びんぼう – poverty, destitute, poor
歩,ふ – pawn (in chess or shogi)
不意,ふい – sudden, abrupt, unexpected, unforeseen
封,ふう – seal
封鎖,ふうさ – blockade, freezing (funds)
風習,ふうしゅう – custom
風俗,ふうぞく – 1. manners, customs, 2. sex service, sex industry
風土,ふうど – natural features, topography, climate, spiritual features
不可欠,ふかけつ – indispensable, essential
深める,ふかめる – to deepen, to heighten, to intensify
不吉,ふきつ – ominous, sinister, bad luck, ill omen, inauspiciousness
不況,ふきょう – recession, depression, slump
布巾,ふきん – tea-towel, dish cloth
福,ふく – good fortune
復旧,ふくきゅう – restoration, restitution, rehabilitation
複合,ふくごう – composite, complex
福祉,ふくし – welfare, well-being
覆面,ふくめん – mask, veil, disguise
膨れる,ふくれる – to get cross, to get sulky, to swell (out), to expand, to be inflated, to distend, to bulge
不景気,ふけいき – business recession, hard times, depression, gloom, sullenness, cheerlessness
老ける,ふける – to age
布告,ふこく – edict, ordinance, proclamation
富豪,ふごう – wealthy person, millionaire
負債,ふさい – debt, liabilities
相応しい,ふさわしい – appropriate
不在,ふざい – absence
不山戯る,ふざける – to romp, to gambol, to frolic, to joke, to make fun of, to flirt
負傷,ふしょう – injury, wound
不審,ふしん – incomplete understanding, doubt, question, distrust, suspicion, strangeness, infidelity
不振,ふしん – dullness, depression, slump, stagnation
不順,ふじゅん – irregularity, unseasonableness
付属,ふぞく – attached, belonging, affiliated, annexed, associated, subordinate, incidental, dependent, auxiliary
負担,ふたん – burden, charge, responsibility
不調,ふちょう – bad condition, not to work out (ie a deal), disagreement, break-off, disorder, slump, out of form
復活,ふっかつ – revival (e.g. musical), restoration
復興,ふっこう – revival, renaissance, reconstruction
沸騰,ふっとう – boiling, seething
仏,ふつ – French
不図,ふと – suddenly, casually, accidentally, incidentally, unexpectedly, unintentionally
不当,ふとう – injustice, impropriety, unreasonableness, undeservedness, unfair, invalid
不動産,ふどうさん – real estate
赴任,ふにん – (proceeding to) new appointment
腐敗,ふはい – decay, depravity
不評,ふひょう – bad reputation, disgrace, unpopularity
不便,ふびん – pity, compassion
不服,ふふく – dissatisfaction, discontent, disapproval, objection, complaint, protest, disagreement
普遍,ふへん – universality, ubiquity, omnipresence
踏まえる,ふまえる – to be based on, to have origin in
文,ふみ – letter, writings
不明,ふめい – unknown, obscure, indistinct, uncertain, ambiguous, ignorant, lack of wisdom, anonymous, unidentified
扶養,ふよう – support, maintenance
振り,ふり – pretence, show, appearance
振り出し,ふりだし – outset, starting point, drawing or issuing (draft)
不良,ふりょう – badness, delinquent, inferiority, failure
浮力,ふりょく – buoyancy, floating power
震わせる,ふるわせる – to be shaking, to be trembling
付録,ふろく – appendix, supplement
分,ふん – minute
憤慨,ふんがい – indignation, resentment
紛失,ふんしつ – losing something
噴出,ふんしゅつ – spewing, gushing, spouting, eruption, effusion
紛争,ふんそう – dispute, trouble, strife
,ふんだん – plentiful, abundant, lavish
奮闘,ふんとう – hard struggle, strenuous effort
粉末,ふんまつ – fine powder
部,ぶ – department, part, category, counter for copies of a newspaper or magazine
部下,ぶか – subordinate person
,ぶかぶか – too big, baggy
侮辱,ぶじょく – insult, contempt, slight
武装,ぶそう – arms, armament, armed
斑,ぶち – spots, speckles, mottles
物資,ぶっし – goods, materials
物体,ぶったい – body, object
物議,ぶつぎ – public discussion (criticism)
打付ける,ぶつける – to knock, to run into, to nail on, to strike hard, to hit and attack
仏像,ぶつぞう – Buddhist image (statue)
無難,ぶなん – safety, security
部門,ぶもん – class, group, category, department, field, branch
ぶら下げる,ぶらさげる – to hang, to suspend, to dangle, to swing
,ぶらぶら – dangle heavily, swing, sway to and fro, aimlessly, idly, lazily, loiter, loaf, be idle, stroll idly
武力,ぶりょく – armed might, military power, the sword, force
無礼,ぶれい – impolite, rude
文化財,ぶんかざい – cultural assets, cultural property
分業,ぶんぎょう – division of labor, specialization, assembly-line production
文語,ぶんご – written language, literary language
分散,ぶんさん – dispersion, decentralization, variance (statistics)
分子,ぶんし – numerator, molecule
文書,ぶんしょ – document, writing, letter, note, records, archives
分担,ぶんたん – apportionment, sharing
分配,ぶんぱい – division, sharing
分母,ぶんぼ – denominator
分離,ぶんり – separation, detachment, segregation, isolation
分裂,ぶんれつ – split, division, break up
兵器,へいき – arms, weapons, ordinance
閉口,へいこう – shut mouth
平行,へいこう – (going) side by side, concurrent, abreast, at the same time, occurring together, parallel, parallelism
閉鎖,へいさ – closing, closure, shutdown, lockout, unsociable
兵士,へいし – soldier
平常,へいじょう – normal, usual
平方,へいほう – square (e.g. metre), square
並列,へいれつ – arrangement, parallel, abreast
辟易,へきえき – wince, shrink back, succumbing to, being frightened, disconcerted
臍,へそ – navel, belly-button
隔たる,へだたる – to be distant
謙る,へりくだる – to deprecate oneself and praise the listener
経る,へる – to pass, to elapse, to experience
編,へん – compilation, editing, completed poem, book, part of book
偏,へん – side, left radical of a character, inclining, inclining toward, biased
変革,へんかく – change, reform, revolution, upheaval, (the) Reformation
返還,へんかん – return, restoration
偏見,へんけん – prejudice, narrow view
返済,へんさい – repayment
変遷,へんせん – change, transition, vicissitudes
返答,へんとう – reply
変動,へんどう – change, fluctuation
弁解,べんかい – explanation, justification, defence, excuse
便宜,べんぎ – convenience, accommodation, advantage, expedience
弁護,べんご – defense, pleading, advocacy
弁償,べんしょう – next word, compensation, reparation, indemnity, reimbursement
弁論,べんろん – discussion, debate, argument
,ぺこぺこ – fawn, be very hungry
穂,ほ – ear (of plant), head (of plant)
保育,ほいく – nursing, nurturing, rearing, lactation, suckling
倣,ほう – imitate, follow, emulate
法案,ほうあん – bill (law)
崩壊,ほうかい – collapse, decay (physics), crumbling, breaking down, caving in
法学,ほうがく – law, jurisprudence
放棄,ほうき – abandonment, renunciation, abdication (responsibility right)
宝器,ほうき – treasured article or vessel, outstanding individual
封建,ほうけん – feudalistic
豊作,ほうさく – abundant harvest, bumper crop
方策,ほうさく – plan, policy
奉仕,ほうし – attendance, service
方式,ほうしき – form, method, system
放射,ほうしゃ – radiation, emission
放射能,ほうしゃのう – radioactivity
報酬,ほうしゅう – remuneration, recompense, reward, toll
放出,ほうしゅつ – release, emit
報じる,ほうじる – to inform, to report
報ずる,ほうずる – to inform, to report
放置,ほうち – leave as is, leave to chance, leave alone, neglect
法廷,ほうてい – courtroom
報道,ほうどう – information, report
褒美,ほうび – reward, prize
葬る,ほうむる – to bury, to inter, to entomb, to consign to oblivion, to shelve
放り込む,ほうりこむ – to throw into
放り出す,ほうりだす – to throw out, to fire, to expel, to give up, to abandon, to neglect
飽和,ほうわ – saturation
保温,ほおん – retaining warmth, keeping heat in, heat insulation
捕獲,ほかく – capture, seizure
保管,ほかん – charge, custody, safekeeping, deposit, storage
補給,ほきゅう – supply, supplying, replenishment
補強,ほきょう – compensation, reinforcement
保険,ほけん – insurance, guarantee
捕鯨,ほげい – whaling, whale fishing
誇る,ほこる – to boast of, to be proud of
綻びる,ほころびる – to come apart at the seams, to begin to open, to smile broadly
保護,ほご – care, protection, shelter, guardianship, favor, patronage
乾,ほし – dried, cured
干し物,ほしもの – dried washing (clothes)
保守,ほしゅ – conservative, maintaining
保障,ほしょう – guarantee, security, assurance, pledge, warranty
補償,ほしょう – compensation, reparation
補充,ほじゅう – supplementation, supplement, replenishment, replenishing
補助,ほじょ – assistance, support, aid, auxiliary
舗装,ほそう – pavement, road surface
補足,ほそく – supplement, complement
発作,ほっさ – fit, spasm
,ほっと – feel relieved
頬っぺた,ほっぺた – cheek
辺り,ほとり – (in the) neighbourhood, vicinity, nearby
殆ど,ほとんど – mostly, almost
解く,ほどく – to unfasten
施す,ほどこす – to donate, to give, to conduct, to apply, to perform
保母,ほぼ – day care worker in a kindergarten nursery school etc.
保養,ほよう – health preservation, recuperation, recreation
捕吏,ほり – constable
捕虜,ほりょ – prisoner (of war)
滅びる,ほろびる – to be ruined, to go under, to perish, to be destroyed
滅ぼす,ほろぼす – to destroy, to overthrow, to wreck, to ruin
本格,ほんかく – propriety, fundamental rules
本館,ほんかん – main building
本気,ほんき – seriousness, truth, sanctity
本質,ほんしつ – essence, true nature, reality
本体,ほんたい – substance, real form, object of worship
本音,ほんね – real intention, motive
本の,ほんの – mere, only, just
本能,ほんのう – instinct
本場,ほんば – home, habitat, center, best place, genuine
本文,ほんぶん – text (of document), body (of letter)
本名,ほんみょう – real name
卯,ぼう – fourth sign of Chinese zodiac (The Hare 5am-7am east February)
防衛,ぼうえい – defense, protection, self-defense
防火,ぼうか – fire prevention, fire fighting, fire proof
妨害,ぼうがい – disturbance, obstruction, hindrance, jamming, interference
紡績,ぼうせき – spinning
呆然,ぼうぜん – dumbfounded, overcome with surprise, in blank amazement
膨脹,ぼうちょう – expansion, swelling, increase, growth
冒頭,ぼうとう – beginning, start, outset
暴動,ぼうどう – insurrection, rebellion, revolt, riot, uprising
暴風,ぼうふう – storm, windstorm, gale
暴力,ぼうりょく – violence
募金,ぼきん – fund-raising, collection of funds
牧師,ぼくし – pastor, minister, clergyman
母校,ぼこう – alma mater
没収,ぼっしゅう – forfeited
坊ちゃん,ぼっちゃん – son (of others)
,ぼつぼつ – gradually, here and there, spots, pimples
没落,ぼつらく – ruin, fall, collapse
,ぼやく – to grumble, to complain
,ぼやける – to become dim, to become blurred
藍褸,ぼろ – rag, scrap, tattered clothes, fault (esp. in a pretense), defect, run-down or junky
枚,まい – counter for flat objects (e.g. sheets of paper)
埋蔵,まいぞう – buried property, treasure trove
舞う,まう – to dance, to flutter about, to revolve
真上,まうえ – just above, right overhead
前売り,まえうり – advance sale, booking
前置き,まえおき – preface, introduction
前もって,まえもって – in advance, beforehand, previously
任す,まかす – to entrust, to leave to a person
負かす,まかす – to defeat
賄う,まかなう – to give board to, to provide meals, to pay
曲がる,まがる – to turn, to bend
巻,まき – volume
紛らわしい,まぎらわしい – confusing, misleading, equivocal, ambiguous
紛れる,まぎれる – to be diverted, to slip into
膜,まく – membrane, film
捲る,まくる – verb suffix to indicate reckless abandon to the activity
真心,まこころ – sincerity, devotion
誠,まこと – truth, faith, fidelity, sincerity, trust, confidence, reliance, devotion
真に,まことに – truly, actually, really
,まごつく – to be confused, to be flustered
正しく,まさしく – surely, no doubt, evidently
正に,まさに – correctly, surely
勝る,まさる – to excel, to surpass, to outrival
増し,まし – extra, additional, less objectionable, better, preferable
真下,ました – right under, directly below
況して,まして – still more, still less (with neg. verb), to say nothing of, not to mention
交える,まじえる – to mix, to converse with, to cross (swords)
交わる,まじわる – to cross, to intersect, to associate with, to mingle with, to interest, to join
麻酔,ますい – anaesthesia
益々,ますます – increasingly, more and more
不味い,まずい – unappetising, unpleasant (taste appearance situation), ugly, unskilful, awkward, bungling, unwise, untime
股,また – groin, crotch, thigh
跨がる,またがる – to extend over or into, to straddle
跨ぐ,またぐ – to straddle
瞬き,またたき – wink, twinkling (of stars), flicker (of light)
待ち合わせ,まちあわせ – appointment
間違う,まちがう – to make a mistake, to be incorrect, to be mistaken
待ち遠しい,まちどおしい – looking forward to
待ち望む,まちのぞむ – to look anxiously for, to wait eagerly for
区々,まちまち – 1. several, various, divergent, conflicting, different, diverse, 2. trivial
末期,まっき – closing years (period days), last stage
真っ二つ,まっぷたつ – in two equal parts
的,まと – mark, target
纏まり,まとまり – conclusion, settlement, consistency
纏め,まとめ – settlement, conclusion
免れる,まぬかれる – to escape from, to be rescued from, to avoid, to evade, to avert, to elude, to be exempted, to be relieved
招き,まねき – invitation
麻痺,まひ – paralysis, palsy, numbness, stupor
眩しい,まぶしい – dazzling, radiant
目蓋,まぶた – eyelid
間々,まま – occasionally, frequently
間もなく,まもなく – soon, before long, in a short time
眉,まゆ – eyebrow
鞠,まり – ball
丸ごと,まるごと – in its entirety, whole, wholly
丸っきり,まるっきり – completely, perfectly, just as if
丸で,まるで – quite, entirely, completely, at all, as if, as though, so to speak
丸々,まるまる – completely
丸める,まるめる – to make round, to round off, to roll up, to curl up, to seduce, to cajole, to explain away
満月,まんげつ – full moon
満場,まんじょう – unanimous, whole audience
真ん中,まんなか – middle, centre, mid-way
真ん前,まんまえ – right in front, under the nose
真ん丸い,まんまるい – perfectly circular
三,み – (num) three
見合い,みあい – formal marriage interview
見合わせる,みあわせる – to exchange glances, to postpone, to suspend operations, to refrain from performing an action
見落とす,みおとす – to overlook, to fail to notice
未開,みかい – savage land, backward region, uncivilized
味覚,みかく – taste, palate, sense of taste
見掛ける,みかける – to (happen to) see, to notice, to catch sight of
三日月,みかずき – new moon, crescent moon
見方,みかた – viewpoint
見苦しい,みぐるしい – unsightly, ugly
見込み,みこみ – hope, prospects, expectation
未婚,みこん – unmarried
惨め,みじめ – miserable
未熟,みじゅく – inexperience, unripeness, raw, unskilled, immature, inexperienced
微塵,みじん – particle, atom
見すぼらしい,みすぼらしい – shabby, seedy
見せびらかす,みせびらかす – to show off, to flaunt
見せ物,みせもの – show, exhibition
満たす,みたす – to satisfy, to ingratiate, to fill, to fulfill
乱す,みだす – to throw out of order, to disarrange, to disturb
乱れる,みだれる – to get confused, to be disordered, to be disturbed
未知,みち – not yet known
導く,みちびく – to be guided, to be shown
身近,みぢか – near oneself, close to one, familiar
密集,みっしゅう – crowd, close formation, dense
密接,みっせつ – related, connected, close, intimate
見っともない,みっともない – shameful, indecent
蜜,みつ – nectar, honey
密度,みつど – density
見積り,みつもり – estimation, quotation
未定,みてい – not yet fixed, undecided, pending
見通し,みとおし – perspective, unobstructed view, outlook, forecast, prospect, insight
源,みなもと – source, origin
身なり,みなり – personal appearance
峰,みね – peak, ridge
見逃す,みのがす – to miss, to overlook, to leave at large
見晴らし,みはらし – view
身振り,みぶり – gesture
見舞,みまい – enquiry, expression of sympathy, expression of concern
脈,みゃく – pulse
未練,みれん – lingering affection, attachment, regret(s), reluctance
見渡す,みわたす – to look out over, to survey (scene), to take an extensive view of
民主,みんしゅ – democratic, the head of the nation
民宿,みんしゅく – private home providing lodging for travelers
民族,みんぞく – people, race, nation, racial customs, folk customs
民俗,みんぞく – people, race, nation, racial customs, folk customs
六,む – (num) six
無意味,むいみ – nonsense, no meaning
向き,むき – direction, situation, exposure, aspect, suitability
無口,むくち – reticence
向け,むけ – for ~, oriented towards ~
婿,むこ – son-in-law
無効,むこう – invalid, no effect, unavailable
無言,むごん – silence
毟る,むしる – to pluck, to pick, to tear
無邪気,むじゃき – innocence, simple-mindedness
結び,むすび – ending, conclusion, union
結び付き,むすびつき – connection, relation
結び付く,むすびつく – to be connected or related, to join together
結び付ける,むすびつける – to combine, to join, to tie on, to attach with a knot
無線,むせん – wireless, radio
無駄遣い,むだづかい – waste money on, squander money on, flog a dead horse
無断,むだん – without permission, without notice
無知,むち – ignorance
無茶,むちゃ – absurd, unreasonable, excessive, rash, absurdity, nonsense
無茶苦茶,むちゃくちゃ – confused, jumbled, mixed up, unreasonable
空しい,むなしい – vacant, futile, vain, void, empty, ineffective, lifeless
無念,むねん – chagrin, regret
無能,むのう – inefficiency, incompetence
無闇に,むやみに – unreasonably, absurdly, recklessly, indiscreetly, at random
無用,むよう – useless, futility, needlessness, unnecessariness
群がる,むらがる – to swarm, to gather
無論,むろん – of course, naturally
名産,めいさん – noted product
名称,めいしょう – name
命中,めいちゅう – a hit
名簿,めいぼ – register of names
名誉,めいよ – honor, credit, prestige
明瞭,めいりょう – clarity
明朗,めいろう – bright, clear, cheerful
目方,めかた – weight
恵み,めぐみ – blessing
恵む,めぐむ – to bless, to show mercy to
目覚しい,めざましい – brilliant, splendid, striking, remarkable
目覚める,めざめる – to wake up
召す,めす – to call, to send for, to put on, to wear, to take (a bath), to ride in, to buy, to eat, to drink, to catch (a
雌,めす – female (animal)
滅茶苦茶,めちゃくちゃ – absurd, unreasonable, excessive, messed up, spoiled, wreaked
目付き,めつき – look, expression of the eyes, eyes
滅亡,めつぼう – downfall, ruin, collapse, destruction
愛でたい,めでたい – auspicious
目眩,めまい – dizziness, giddiness
目盛,めもり – scale, gradations
面会,めんかい – interview
免除,めんじょ – exemption, exoneration, discharge
面する,めんする – to face on, to look out on to
面目,めんぼく – face, honour, reputation, prestige, dignity, credit
設ける,もうける – to create, to establish
申し入れる,もうしいれる – to propose, to suggest
申し込み,もうしこみ – application, entry, request, subscription, offer, proposal, overture, challenge
申出,もうしで – proposal, request, claim, report, notice
申し出る,もうしでる – to report to, to tell, to suggest, to submit, to request, to make an offer, to come forward with informati
申し分,もうしぶん – objection, shortcomings
盲点,もうてん – blind spot
猛烈,もうれつ – violent, vehement, rage
藻掻く,もがく – to struggle, to wriggle, to be impatient
目録,もくろく – catalogue, catalog, list
目論見,もくろみ – a plan, a scheme, a project, a program, intention, goal
模型,もけい – model, dummy, maquette
模索,もさく – groping (for)
若し,もし – if, in case, supposing
若しかしたら,もしかしたら – perhaps, maybe, by some chance
若しかして,もしかして – perhaps, possibly
若しかすると,もしかすると – perhaps, maybe, by some chance
若しくは,もしくは – or, otherwise
若しも,もしも – if
齎らす,もたらす – to bring, to take, to bring about
凭れる,もたれる – to lean against, to lean on, to recline on, to lie heavy (on the stomach)
持ち,もち – 1. hold, charge, keep possession, in charge, 2. wear, durability, life, draw, 3. usage (suff)
持ち切り,もちきり – hot topic, talk of the town
物体ない,もったいない – too good, more than one deserves, wasteful, sacrilegious, unworthy of
以て,もって – with, by, by means of, because, in view of
専ら,もっぱら – wholly, solely, entirely
持て成す,もてなす – to entertain, to make welcome
持てる,もてる – to be well liked, to be popular
基,もとい – basis
物置き,ものおき – storeroom
物好き,ものずき – curiosity
物足りない,ものたりない – unsatisfied, unsatisfactory
最早,もはや – already, now
模範,もはん – exemplar, exemplification, exemplum, model, example
模倣,もほう – imitation, copying
揉める,もめる – to disagree, to dispute
腿,もも – thigh, femur
催す,もよおす – to hold (a meeting), to give (a dinner), to feel, to show signs of, to develop symptoms of, to feel (sick
漏らす,もらす – to let leak, to reveal
盛り上がる,もりあがる – to rouse, to swell, to rise
漏る,もる – to leak, to run out
漏れる,もれる – to leak out, to escape, to come through, to shine through, to filter out, to be omitted
脆い,もろい – brittle, fragile, tender-hearted
,もろに – completely, all the way
問,もん – problem, question
矢,や – arrow
哉,や – question mark
喧しい,やかましい – noisy, strict, fussy
野外,やがい – fields, outskirts, open air, suburbs
軈て,やがて – before long, soon, at length
夜行,やぎょう – walking around at night, night train, night travel
役職,やくしょく – post, managerial position, official position
役立つ,やくだつ – to be useful, to be helpful, to serve the purpose
役場,やくば – town hall
夜具,やぐ – bedding
優,やさ – gentle, affectionate
屋敷,やしき – mansion
養う,やしなう – to rear, to maintain, to cultivate
社,やしろ – Shinto shrine
野心,やしん – ambition, aspiration, designs, treachery
易い,やすい – easy
安っぽい,やすっぽい – cheap-looking, tawdry, insignificant
休める,やすめる – to rest, to suspend, to give relief
野生,やせい – wild
矢鱈に,やたらに – randomly, recklessly, blindly
夜中,やちゅう – all night, the whole night
奴,やっこ – servant, fellow
やっ付ける,やっつける – to beat
矢っ張り,やっぱり – also, as I thought, still, in spite of, absolutely
野党,やとう – opposition party
病,やまい – illness, disease
闇,やみ – darkness, the dark, black-marketeering, dark, shady, illegal
病む,やむ – to fall ill, to be ill
止むを得ない,やむをえない – cannot be helped, unavoidable
稍,やや – a little, partially, somewhat, a short time, a while
,ややこしい – puzzling, tangled, complicated, complex
遣り通す,やりとおす – to carry through, to achieve, to complete
やり遂げる,やりとげる – to accomplish
遣る,やる – to do, to have sexual intercourse, to kill, to give (to inferiors animals etc.), to dispatch (a letter
和らげる,やわらげる – to soften, to moderate, to relieve
優位,ゆうい – predominance, ascendancy, superiority
憂鬱,ゆううつ – depression, melancholy, dejection, gloom
有益,ゆうえき – beneficial, profitable
優越,ゆうえつ – supremacy, predominance, being superior to
勇敢,ゆうかん – bravery, heroism, gallantry
有機,ゆうき – organic
夕暮れ,ゆうぐれ – evening, (evening) twilight
融資,ゆうし – financing, loan
有する,ゆうする – to own, to be endowed with
融通,ゆうずう – lending (money), accommodation, adaptability, versatility, finance
優勢,ゆうせい – superiority, superior power, predominance, preponderance
優先,ゆうせん – preference, priority
誘導,ゆうどう – guidance, leading, induction, introduction, incitement, inducement
優美,ゆうび – grace, refinement, elegance
有望,ゆうぼう – good prospects, full of hope, promising
遊牧,ゆうぼく – nomadism
夕焼け,ゆうやけ – sunset
有力,ゆうりょく – 1. influence, prominence, 2. potent
幽霊,ゆうれい – ghost, specter, apparition, phantom
誘惑,ゆうわく – temptation, allurement, lure
揺さぶる,ゆさぶる – to shake, to jolt, to rock, to swing
茹でる,ゆでる – to boil
,ゆとり – reserve, affluence, room, time (to spare)
指差す,ゆびさす – to point at
弓,ゆみ – bow (and arrow)
揺らぐ,ゆらぐ – to swing, to sway, to shake, to tremble
緩む,ゆるむ – to become loose, to slacken
緩める,ゆるめる – to loosen, to slow down
緩やか,ゆるやか – lenient
世,よ – world, society, age, generation
好い,よい – good
要因,よういん – primary factor, main cause
溶液,ようえき – solution (liquid)
用件,ようけん – business
養護,ようご – protection, nursing, protective care
用紙,ようし – blank form
様式,ようしき – style, form, pattern
要する,ようする – to demand, to require, to take
要請,ようせい – claim, demand, request, application
養成,ようせい – training, development
様相,ようそう – aspect
用品,ようひん – articles, supplies, parts
洋風,ようふう – western style
用法,ようほう – directions, rules of use
要望,ようぼう – demand for, request
余暇,よか – leisure, leisure time, spare time
予感,よかん – presentiment, premonition
余興,よきょう – side show, entertainment
預金,よきん – deposit, bank account
抑圧,よくあつ – check, restraint, oppression, suppression
浴室,よくしつ – bathroom, bath
抑制,よくせい – suppression
欲深い,よくふかい – greedy
欲望,よくぼう – desire, appetite
寄こす,よこす – to send, to forward
横綱,よこづな – sumo grand champion
葦,よし – reed, bulrush
善し悪し,よしあし – good or bad, merits or demerits, quality, suitability
予想,よそう – expectation, anticipation, prediction, forecast
余所見,よそみ – looking away, looking aside
余地,よち – place, room, margin, scope
依って,よって – therefore, consequently, accordingly, because of
余程,よっぽど – very, greatly, much, to a large extent, quite
与党,よとう – government party, (ruling) party in power, government
呼び止める,よびとめる – to challenge, to call somebody to halt
夜更かし,よふかし – staying up late, keeping late hours, sitting up late at night, nighthawk
夜更け,よふけ – late at night
読み上げる,よみあげる – to read out loud (and clearly), to call a roll
寄り掛かる,よりかかる – to lean against, to recline on, to lean on, to rely on
宜しく,よろしく – well, properly, suitably, best regards, please remember me
弱まる,よわまる – to abate, to weaken, to be emaciated, to be dejected, to be perplexed
弱める,よわめる – to weaken
弱る,よわる – to weaken, to be troubled, to be downcast, to be emaciated, to be dejected, to be perplexed, to impair
来場,らいじょう – attendance
酪農,らくのう – dairy (farm)
落下,らっか – fall, drop, come down
楽観,らっかん – optimism
濫用,らんよう – abuse, misuse, misappropriation, using to excess
理屈,りくつ – theory, reason
利根,りこん – intelligence
利子,りし – interest (bank)
利潤,りじゅん – profit, returns
理性,りせい – reason, sense
利息,りそく – interest (bank)
立体,りったい – solid body
立法,りっぽう – legislation, lawmaking
利点,りてん – advantage, point in favor
略語,りゃくご – abbreviation, acronym
略奪,りゃくだつ – pillage, plunder, looting, robbery
流,りゅう – styleof, method of, manner of
流通,りゅうつう – circulation of money or goods, flow of water or air, distribution
了,りょう – finish, completion, understanding
料,りょう – material, charge, rate, fee
領域,りょういき – area, domain, territory, field, region, regime
了解,りょうかい – comprehension, consent, understanding, roger (on the radio)
領海,りょうかい – territorial waters
両極,りょうきょく – both extremities, north and south poles, positive and negative poles
良好,りょうこう – favorable, satisfactory
良識,りょうしき – good sense
良質,りょうしつ – good quality, superior quality
了承,りょうしょう – acknowledgement, understanding (e.g. please be understanding of the mess during our renovation)
良心,りょうしん – conscience
領地,りょうち – territory, dominion
領土,りょうど – dominion, territory, possession
両立,りょうりつ – compatibility, coexistence, standing together
旅客,りょかく – passenger (transport)
旅券,りょけん – passport
履歴,りれき – personal history, background, career, log
理論,りろん – theory
輪,りん – counter for wheels and flowers
林業,りんぎょう – forestry
類似,るいじ – analogous
類推,るいすい – analogy
冷酷,れいこく – cruelty, coldheartedness, relentless, ruthless
冷蔵,れいぞう – cold storage, refrigeration
冷淡,れいたん – coolness, indifference
恋愛,れんあい – love, love-making, passion, emotion, affections
連休,れんきゅう – consecutive holidays
連日,れんじつ – every day, prolonged
連中,れんじゅう – colleagues, company, a lot
連帯,れんたい – solidarity
連邦,れんぽう – commonwealth, federation of states
連盟,れんめい – league, union, alliance
老衰,ろうすい – senility, senile decay
朗読,ろうどく – reading aloud, recitation
浪費,ろうひ – waste, extravagance
労力,ろうりょく – labour, effort, toil, trouble
碌な,ろくな – satisfactory, decent
碌に,ろくに – well, enough, sufficient
露骨,ろこつ – 1. frank, blunt, plain, outspoken, 2. conspicuous, open, 3. broad, suggestive
論議,ろんぎ – discussion
論理,ろんり – logic
和,わ – sum, harmony, peace
我がまま,わがまま – selfishness, egoism, wilfulness, disobedience, whim
枠,わく – frame, slide
惑星,わくせい – planet
技,わざ – art, technique
態と,わざと – on purpose
態々,わざわざ – expressly, specially, doing something especially rather than incidentally
煩わしい,わずらわしい – troublesome, annoying, complicated
渡り鳥,わたりどり – migratory bird, bird of passage
詫び,わび – apology
和風,わふう – Japanese style
和文,わぶん – Japanese text, sentence in Japanese
藁,わら – straw
割合に,わりあいに – comparatively
割り当て,わりあて – allotment, assignment, allocation, quota, rationing
割り込む,わりこむ – to cut in, to thrust oneself into, to wedge oneself in, to muscle in on, to interrupt, to disturb
割り算,わりざん – division (math)
割引き,わりびき – discount, reduction, rebate, tenths discounted
悪者,わるもの – bad fellow, rascal, ruffian, scoundrel
"""

def notify(title, text):
	os.system("""
		osascript -e 'display notification "{}" with title "{}"'
	""".format(text, title))

lines       = dataset.split("\n")
lines       = [line.split("–") for line in lines if line]
random.shuffle(lines)
choice      = random.choice(lines)

japan_word  = choice[0]
explanation = choice[1]

notify(japan_word, explanation)
