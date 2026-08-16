import os
import json

# Comprehensive Quiz Database for ALL lessons across subjects, including new MabKom categories from 'more'
ALL_LESSON_QUIZZES = {
    # ================= MABISANG KOMUNIKASYON =================
    "mk-elem-anyo": {
        "title": "Aralin 3.1: 5 Elemento at Anyo ng Pagpapahayag",
        "lessonId": "lesson-mk-elem-anyo",
        "questions": [
            {
                "q": "Sino ang pinagmumulan o nagpapadala ng mensahe?",
                "options": ["Tagatanggap (Receiver)", "Tagapagpadala (Sender)", "Daluyan (Channel)", "Tugon (Feedback)"],
                "answer": 1,
                "hint": "Ang Sender ang nagsisimula ng proseso."
            },
            {
                "q": "Aling anyo ng pagpapahayag ang nagbibigay ng impormasyon batay sa nakita o narinig NANG HINDI AGAD NAGBIBIGAY NG SARILING PAGHUHUSGA?",
                "options": ["Pagkukuwento", "Paglalahad ng Obserbasyon", "Pagtatanong", "Panghuhula"],
                "answer": 1,
                "hint": "Obserbasyon muna bago humusga."
            },
            {
                "q": "'Ano po ang takdang-aralin?' ay halimbawa ng anong anyo ng pagpapahayag?",
                "options": ["Pagpapahayag ng Opinyon", "Pagkukuwento", "Pagtatanong", "Paglalahad ng Obserbasyon"],
                "answer": 2,
                "hint": "Paraan ng pagkuha ng impormasyon o paghingi ng linaw."
            },
            {
                "q": "Ang pagsasalaysay ng isang karanasan o pangyayari upang magbahagi ng impormasyon o magbigay-aliw ay:",
                "options": ["Pagtatanong", "Pagkukuwento", "Tugon", "Noise"],
                "answer": 1,
                "hint": "Pagsasalaysay ng kwento at karanasan."
            }
        ]
    },
    "mk-antas-awdyens": {
        "title": "Aralin 3.2: Antas ng Komunikasyon at Awdyens",
        "lessonId": "lesson-mk-antas-awdyens",
        "questions": [
            {
                "q": "Ano ang tawag sa komunikasyon kung saan iisa ang tagapagsalita at marami ang tagapakinig?",
                "options": ["Personal na Komunikasyon", "Interpersonal na Komunikasyon", "Pampublikong Komunikasyon", "Passive Footprint"],
                "answer": 2,
                "hint": "Pampubliko dahil nakatuon sa malaking madla tulad ng talumpati."
            },
            {
                "q": "Bakit mahalagang kilalanin ang awdyens bago magpahayag?",
                "options": ["Upang malaman ang kanilang password", "Upang makapili ng angkop na salita, tono, at paraan ng pagpapahayag", "Para sumikat online", "Para maiwasan ang pagsasalita"],
                "answer": 1,
                "hint": "Dapat iakma ang tono at wika sa nakikinig."
            },
            {
                "q": "Saan karaniwang ginagamit ang PORMAL na wika?",
                "options": ["Chat sa barkada", "Paaralan, opisina, at talumpati", "Kaswal na usapan sa kanto", "TikTok comments"],
                "answer": 1,
                "hint": "Ginagamit sa opisyal at seryosong sitwasyon."
            },
            {
                "q": "Alin ang mas SISTEMATIKONG pagsulat ng mga natutuhan, obserbasyon, at pagninilay sa sarili?",
                "options": ["Dyornal (Journal)", "Talaarawan (Diary)", "Blog Comment", "Tweet"],
                "answer": 0,
                "hint": "Dyornal ang mas nakatuon sa sistematikong pagkatuto."
            }
        ]
    },
    "mk-digital-privacy": {
        "title": "Aralin 3.3: Digital Identity, Privacy at Netiquette",
        "lessonId": "lesson-mk-digital-privacy",
        "questions": [
            {
                "q": "Ano ang kahulugan ng PRIVACY (Pagkapribado)?",
                "options": ["Karapatang mag-post ng kahit ano", "Karapatan ng tao na panatilihing pribado at ligtas ang kaniyang personal na impormasyon", "Pagbura ng account", "Pagbabahagi ng password"],
                "answer": 1,
                "hint": "Pangangalaga sa sariling impormasyon."
            },
            {
                "q": "Alin ang halimbawa ng PASSIVE digital footprint?",
                "options": ["Pag-upload ng video", "Web cookies at browsing history na awtomatikong nakokolekta", "Pag-post ng status", "Pagkomento sa balita"],
                "answer": 1,
                "hint": "Awtomatikong naitatala nang walang kusa."
            },
            {
                "q": "Bakit mahalaga ang Two-Factor Authentication (2FA) at Personal Data Protection?",
                "options": ["Upang maprotektahan ang datos laban sa hindi awtorisadong paggamit", "Upang dumami ang followers", "Upang bumilis ang phone", "Upang maging pormal ang chat"],
                "answer": 0,
                "hint": "Karagdagang layer ng seguridad sa personal data."
            }
        ]
    },
    "mk-public-facing": {
        "title": "Aralin 3.4: Public-Facing na Teksto at Layunin Nito",
        "lessonId": "lesson-mk-public-facing",
        "questions": [
            {
                "q": "Aling public-facing text ang naglalayong HIKAYATIN ang mga tao na suportahan o makiisa sa isang adbokasiya?",
                "options": ["Talaarawan", "Advocacy Post", "Maikling Kolumn", "Dyornal"],
                "answer": 1,
                "hint": "Advocacy post ang humihikayat sa layunin."
            },
            {
                "q": "Ano ang INCLUSIVITY (Pagiging Inklusibo) bilang layunin ng teksto?",
                "options": ["Pagbubukod sa mga mahihirap", "Pantay na paggalang, pagkakataon, at pagtanggap sa lahat anuman ang kasarian, edad, o kultura", "Pagsasara ng komento", "Pang-iinsulto sa iba"],
                "answer": 1,
                "hint": "Pantay na pagtanggap sa lahat nang walang diskriminasyon."
            },
            {
                "q": "Ang maikling artikulo na nagpapahayag ng opinyon ng may-akda sa napapanahong isyu ay tinatawag na:",
                "options": ["Blog", "Maikling Kolumn", "Advocacy Post", "Talaarawan"],
                "answer": 1,
                "hint": "Maikling kolumn sa pahayagan o magasin."
            },
            {
                "q": "Alin ang sulating nagbibigay ng sariling pananaw, pagsusuri, o opinyon tungkol sa isang balita o isyu?",
                "options": ["Komentaryo", "Data Protection", "2FA", "Passive Footprint"],
                "answer": 0,
                "hint": "Komentaryo ang naglalaman ng pagsusuri at pananaw."
            }
        ]
    },
    "mk-proseso": {
        "title": "Aralin 4.1: Dinamikong Proseso ng Komunikasyon",
        "lessonId": "lesson-mk-proseso",
        "questions": [
            {
                "q": "Alin sa 3 proseso ang tumutukoy sa pag-unawa at pagbibigay-kahulugan sa mensahe batay sa karanasan at emosyon?",
                "options": ["Pagpapahayag (Expression)", "Pakikilahok (Participation)", "Pagbibigay-kahulugan (Decoding)", "Pampubliko"],
                "answer": 2,
                "hint": "Decoding ang pag-unawa sa kahulugan."
            },
            {
                "q": "Bakit sinasabing DINAMIKO ang komunikasyon?",
                "options": ["Dahil ito ay nakatigil", "Dahil ito ay tuloy-tuloy, interaktibo, at lumulutas ng mga suliranin", "Dahil pasulat lamang ito", "Dahil walang tugon"],
                "answer": 1,
                "hint": "Dinamiko = patuloy na nagbabago at umuunlad ang ugnayan."
            },
            {
                "q": "Ang aktibong pakikinig at pakikiisa sa talakayan ay bahagi ng anong proseso?",
                "options": ["Pakikilahok (Participation)", "Passive Data", "Personal Data", "Noise"],
                "answer": 0,
                "hint": "Pakikilahok = active engagement."
            }
        ]
    },
    "mk-kultural-konteksto": {
        "title": "Aralin 4.2: 4 na Konteksto at Kamalayang Kultural",
        "lessonId": "lesson-mk-kultural-konteksto",
        "questions": [
            {
                "q": "Ang komunikasyon sa loob ng pangkat o komunidad (hal. pagbibigay ng opinyon sa klase) ay kontekstong:",
                "options": ["Personal", "Interpersonal", "Sosyal", "Kultural"],
                "answer": 2,
                "hint": "Sosyal ang antas sa pangkat o komunidad."
            },
            {
                "q": "Aling pahayag ang nagpapakita ng SENSIBILIDAD sa komunikasyon?",
                "options": ["'Maling-mali ka!'", "'Wala kang alam!'", "'Mayroon akong ibang pananaw ukol diyan.'", "'Tumahimik ka na lang.'"],
                "answer": 2,
                "hint": "Isinasaalang-alang ang damdamin ng kausap."
            },
            {
                "q": "Ang paggamit ng 'po' at 'opo' sa Pilipinas ay halimbawa ng anong konteksto?",
                "options": ["Personal", "Kultural (pag-unawa sa tradisyon at paniniwala)", "Passive Footprint", "Noise"],
                "answer": 1,
                "hint": "Bahagi ito ng kultura at kaugaliang Pilipino."
            }
        ]
    },

    # ================= GENERAL SCIENCE =================
    "gs-levers": {
        "title": "Week 5: The Three Classes of Levers",
        "lessonId": "lesson-gs-levers",
        "questions": [
            {
                "q": "Which class of lever has the FULCRUM in the middle?",
                "options": ["1st Class Lever (Seesaw, scissors)", "2nd Class Lever (Wheelbarrow)", "3rd Class Lever (Tweezers)", "None"],
                "answer": 0,
                "hint": "1st = Fulcrum in middle."
            },
            {
                "q": "Which class of lever has the LOAD in the middle and always has MA > 1?",
                "options": ["1st Class", "2nd Class", "3rd Class", "4th Class"],
                "answer": 1,
                "hint": "2nd = Load in middle."
            },
            {
                "q": "Which class of lever has the EFFORT in the middle and multiplies speed (MA < 1)?",
                "options": ["1st Class", "2nd Class", "3rd Class", "Fixed pulley"],
                "answer": 2,
                "hint": "3rd = Effort in middle."
            }
        ]
    },
    "gs-pulleys": {
        "title": "Week 5: Pulleys, Wheels, & Inclined Planes",
        "lessonId": "lesson-gs-pulleys",
        "questions": [
            {
                "q": "A fixed pulley has a Mechanical Advantage of:",
                "options": ["0", "1 (only redirects force)", "2", "4"],
                "answer": 1,
                "hint": "It changes force direction only."
            },
            {
                "q": "A ramp is 10 m long and 2 m high. What is its Ideal Mechanical Advantage (IMA)?",
                "options": ["0.2", "5", "20", "8"],
                "answer": 1,
                "hint": "IMA = Length / Height (10 / 2 = 5)."
            },
            {
                "q": "Two inclined planes placed back-to-back used for cutting describe a:",
                "options": ["Screw", "Wedge", "Wheel and Axle", "3rd Class Lever"],
                "answer": 1,
                "hint": "Axes and knives are wedges."
            }
        ]
    },
    "gs-compound": {
        "title": "Week 5: Compound Machines & Combined MA",
        "lessonId": "lesson-gs-compound",
        "questions": [
            {
                "q": "How is total MA of a compound machine calculated?",
                "options": ["MA_total = MA1 + MA2", "MA_total = MA1 x MA2 x MA3...", "MA_total = (MA1 + MA2) / 2", "MA_total = MA1 - MA2"],
                "answer": 1,
                "hint": "Multiplied together."
            },
            {
                "q": "Why are compound machines generally less efficient than simple machines?",
                "options": ["They produce too much work", "More moving parts introduce more friction and heat loss", "They violate physics", "They have MA < 1"],
                "answer": 1,
                "hint": "Friction from multiple components."
            },
            {
                "q": "A pair of scissors combines which simple machines?",
                "options": ["Two 1st class levers + wedge blades", "Wheel & axle + pulley", "Screw + ramp", "3rd class lever + fixed pulley"],
                "answer": 0,
                "hint": "Pivoted levers with sharp wedge blades."
            }
        ]
    },
    "gs-pascal": {
        "title": "Week 6: Pascal's Principle & Hydraulics",
        "lessonId": "lesson-gs-pascal",
        "questions": [
            {
                "q": "Pascal's Principle states that pressure applied to an enclosed fluid is:",
                "options": ["Lost at the bottom", "Transmitted undiminished in all directions", "Reduced by 50%", "Directed only upwards"],
                "answer": 1,
                "hint": "P1 = P2 throughout the fluid."
            },
            {
                "q": "In a hydraulic lift, if Piston 2 has 10 times the area of Piston 1, the output force F2 will be:",
                "options": ["10 times greater than F1", "10 times smaller than F1", "Equal to F1", "Zero"],
                "answer": 0,
                "hint": "F2 = F1 x (A2 / A1)."
            },
            {
                "q": "Which machine operates directly on Pascal's Principle?",
                "options": ["Hydraulic car brakes and lifts", "A simple crowbar", "A fixed flagpole pulley", "A compass"],
                "answer": 0,
                "hint": "Hydraulic systems use fluid pressure."
            }
        ]
    },
    "gs-archimedes": {
        "title": "Week 6: Archimedes' Principle & Buoyancy",
        "lessonId": "lesson-gs-archimedes",
        "questions": [
            {
                "q": "According to Archimedes' Principle, Buoyant Force (Fb) equals:",
                "options": ["Total weight of the object", "Weight of fluid displaced by the object", "Depth of the water", "Zero in seawater"],
                "answer": 1,
                "hint": "Fb = Weight of displaced fluid."
            },
            {
                "q": "An object will SINK in water if:",
                "options": ["Its density is greater than water (Fb < Weight)", "Its density is less than water", "It is made of wood", "Its volume is large"],
                "answer": 0,
                "hint": "Higher density sinks."
            },
            {
                "q": "Why do massive steel ships float on water?",
                "options": ["Steel is lighter than water", "Hollow hull displaces huge volume of water, creating large buoyant force", "Salt in ocean repels steel", "Engines push the ship up"],
                "answer": 1,
                "hint": "Displaced water weight exceeds ship weight."
            }
        ]
    },

    # ================= GENERAL MATHEMATICS =================
    "gm-markup": {
        "title": "Week 6: Mark-up, Mark-down & Discounts",
        "lessonId": "lesson-gm-markup",
        "questions": [
            {
                "q": "If an item costs ₱400 and is sold for ₱550, what is the Mark-up?",
                "options": ["₱100", "₱150", "₱950", "₱200"],
                "answer": 1,
                "hint": "Mark-up = 550 - 400 = 150."
            },
            {
                "q": "A ₱1,000 item has a 25% discount. What is the Sale Price?",
                "options": ["₱250", "₱750", "₱1,250", "₱800"],
                "answer": 1,
                "hint": "1,000 - 250 = 750."
            },
            {
                "q": "What is the formula for Mark-up Rate based on Cost?",
                "options": ["(Mark-up / Cost) x 100%", "(Cost / Mark-up) x 100%", "Cost x Selling Price", "Selling Price - Discount"],
                "answer": 0,
                "hint": "Mark-up over original cost."
            }
        ]
    },
    "gm-interest": {
        "title": "Week 6: Simple Interest & Maturity Value",
        "lessonId": "lesson-gm-interest",
        "questions": [
            {
                "q": "What is the formula for Simple Interest (I)?",
                "options": ["I = P + r + t", "I = Prt (Principal x Rate x Time)", "I = P / rt", "I = P(1 + r)^t"],
                "answer": 1,
                "hint": "I = Prt."
            },
            {
                "q": "If you invest ₱20,000 at 4% for 2 years, how much interest is earned?",
                "options": ["₱800", "₱1,600", "₱21,600", "₱4,000"],
                "answer": 1,
                "hint": "20,000 x 0.04 x 2 = 1,600."
            },
            {
                "q": "What is the Maturity Value (Future Value F) of the investment above?",
                "options": ["₱1,600", "₱20,000", "₱21,600", "₱24,000"],
                "answer": 2,
                "hint": "20,000 + 1,600 = 21,600."
            }
        ]
    },
    "gm-patterns": {
        "title": "Week 7: Patterns in Nature & Fibonacci",
        "lessonId": "lesson-gm-patterns",
        "questions": [
            {
                "q": "What are the next two terms: 0, 1, 1, 2, 3, 5, 8, __, __?",
                "options": ["10, 12", "13, 21", "11, 15", "16, 24"],
                "answer": 1,
                "hint": "5+8=13, 8+13=21."
            },
            {
                "q": "Which symmetry is shown by a starfish and sunflower florets?",
                "options": ["Bilateral symmetry", "Radial / Rotational symmetry", "Asymmetry", "Translation"],
                "answer": 1,
                "hint": "Rotational around center."
            },
            {
                "q": "Why do honeybees build hexagonal honeycomb cells?",
                "options": ["Random", "Hexagons maximize storage volume with minimal perimeter/wax", "To trap heat only", "Easier to count"],
                "answer": 1,
                "hint": "Optimal packing efficiency."
            }
        ]
    },
    "gm-sequences": {
        "title": "Week 8: Arithmetic & Geometric Sequences",
        "lessonId": "lesson-gm-sequences",
        "questions": [
            {
                "q": "In the Arithmetic Sequence 5, 9, 13, 17..., what is the Common Difference (d)?",
                "options": ["2", "4", "5", "8"],
                "answer": 1,
                "hint": "d = 9 - 5 = 4."
            },
            {
                "q": "What is the formula for the nth term of an Arithmetic Sequence?",
                "options": ["an = a1 + (n - 1)d", "an = a1 x r^(n-1)", "an = n x d", "an = a1 / d"],
                "answer": 0,
                "hint": "an = a1 + (n - 1)d."
            },
            {
                "q": "In the Geometric Sequence 3, 6, 12, 24..., what is the Common Ratio (r)?",
                "options": ["2", "3", "4", "6"],
                "answer": 0,
                "hint": "r = 6 / 3 = 2."
            }
        ]
    },

    # ================= FINITE MATHEMATICS 1 =================
    "fn-tess": {
        "title": "Lesson 3: Tessellations & Frieze Patterns",
        "lessonId": "lesson-fn-tess",
        "questions": [
            {
                "q": "What is a Tessellation (Tiling)?",
                "options": ["3D sculpture", "Covering a plane with shapes without overlaps or gaps", "Equation", "Fractal dimension"],
                "answer": 1,
                "hint": "No gaps, no overlaps."
            },
            {
                "q": "How many distinct Frieze Symmetry Groups exist in 1D border patterns?",
                "options": ["4", "7", "12", "17"],
                "answer": 1,
                "hint": "Exactly 7 frieze groups."
            },
            {
                "q": "Which transformation slides an object along a line without rotation?",
                "options": ["Reflection", "Rotation", "Translation", "Glide Reflection"],
                "answer": 2,
                "hint": "Linear slide is Translation."
            }
        ]
    },
    "fn-golden": {
        "title": "Lesson 4: Golden Ratio & Fibonacci Spirals",
        "lessonId": "lesson-fn-golden",
        "questions": [
            {
                "q": "What is the approximate value of the Golden Ratio (Phi, φ)?",
                "options": ["3.1416", "1.618", "2.718", "1.414"],
                "answer": 1,
                "hint": "φ ≈ 1.6180339887."
            },
            {
                "q": "A Golden Rectangle has side lengths in the ratio:",
                "options": ["2 : 1", "1.618 : 1 (φ : 1)", "3 : 2", "1 : 1"],
                "answer": 1,
                "hint": "Length / Width = φ."
            },
            {
                "q": "As Fibonacci sequence progresses, the ratio of consecutive terms (Fn+1 / Fn) approaches:",
                "options": ["0", "1", "The Golden Ratio (φ ≈ 1.618)", "Infinity"],
                "answer": 2,
                "hint": "Converges to Phi."
            }
        ]
    },
    "fn-fractals": {
        "title": "Lesson 5: Fractals & Self-Similarity",
        "lessonId": "lesson-fn-fractals",
        "questions": [
            {
                "q": "What is the defining property of a Fractal?",
                "options": ["Straight lines only", "Self-Similarity (repeats structure at every scale)", "Fixed area only", "Finite iterations only"],
                "answer": 1,
                "hint": "Structural repetition across zoom levels."
            },
            {
                "q": "Which of the following is a classic fractal?",
                "options": ["Sierpinski Gasket / Triangle", "Koch Snowflake", "Mandelbrot Set", "All of the above"],
                "answer": 3,
                "hint": "All three are prominent fractals."
            },
            {
                "q": "Which natural phenomenon displays fractal geometry?",
                "options": ["Fern leaves and coastlines", "Lightning branches and river networks", "Blood vessels and lung bronchi", "All of the above"],
                "answer": 3,
                "hint": "Nature uses fractal branching."
            }
        ]
    },
    "fn-matrix": {
        "title": "Lessons 6 & 7: Matrix Algebra & Multiplication",
        "lessonId": "lesson-fn-matrix",
        "questions": [
            {
                "q": "To ADD two matrices, they must have:",
                "options": ["Square dimensions", "Identical dimensions (same rows and columns)", "Determinants equal to 1", "Positive entries only"],
                "answer": 1,
                "hint": "Same m x n order."
            },
            {
                "q": "What condition must be met to MULTIPLY Matrix A (m x k) and Matrix B (p x n)?",
                "options": ["Columns of A (k) must equal Rows of B (p)", "Rows of A must equal Rows of B", "Both must be square", "k must equal m"],
                "answer": 0,
                "hint": "Inner dimensions must match: (m x k) • (k x n)."
            },
            {
                "q": "If Matrix A is (2 x 3) and Matrix B is (3 x 4), what is the order of AB?",
                "options": ["2 x 4", "3 x 3", "2 x 3", "Undefined"],
                "answer": 0,
                "hint": "Outer dimensions: 2 x 4."
            }
        ]
    }
}

print(f"Updated Quiz Database with {len(ALL_LESSON_QUIZZES)} distinct quizzes including all MabKom categories!")
