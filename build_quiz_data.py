import os
import json

# Comprehensive Quiz Database for EVERY lesson/topic
ALL_LESSON_QUIZZES = {
    # ================= MABISANG KOMUNIKASYON =================
    "mk-elem": {
        "title": "Aralin 3: 5 Elemento ng Komunikasyon",
        "lessonId": "lesson-mk-elem",
        "questions": [
            {
                "q": "Sino ang pinagmumulan o nagpapadala ng mensahe?",
                "options": ["Tagatanggap (Receiver)", "Tagapagpadala (Sender)", "Daluyan (Channel)", "Tugon (Feedback)"],
                "answer": 1,
                "hint": "Ang Sender ang nagsisimula ng proseso."
            },
            {
                "q": "Ano ang tawag sa reaksyon o sagot na nagpapatunay kung naunawaan ang mensahe?",
                "options": ["Daluyan", "Mensahe", "Tugon (Feedback)", "Noise"],
                "answer": 2,
                "hint": "Ang Feedback ang nagbabalik ng tugon."
            },
            {
                "q": "Ang online chat, tawag sa telepono, at sulat ay mga halimbawa ng:",
                "options": ["Tagapagpadala", "Daluyan (Channel)", "Tagatanggap", "Tugon"],
                "answer": 1,
                "hint": "Ito ang midyum o paraan ng pagpapadala."
            }
        ]
    },
    "mk-intra": {
        "title": "Aralin 3: Intrapersonal na Komunikasyon",
        "lessonId": "lesson-mk-intra",
        "questions": [
            {
                "q": "Ang intrapersonal na komunikasyon ay pakikipag-usap sa:",
                "options": ["Maraming tao", "Guro at punong-guro", "Sarili", "Social media followers"],
                "answer": 2,
                "hint": "Intra = sa loob ng sarili."
            },
            {
                "q": "Alin ang mas SISTEMATIKONG pagsulat ng mga natutuhan, karanasan, at pagninilay?",
                "options": ["Dyornal (Journal)", "Talaarawan (Diary)", "Chat message", "Advocacy Post"],
                "answer": 0,
                "hint": "Ang Dyornal ay mas nakatutok sa aral at obserbasyon."
            },
            {
                "q": "Ang pagtatakda ng mga nais makamit sa hinaharap ay tinatawag na:",
                "options": ["Repleksyon", "Goal Setting", "Passive footprint", "Netiquette"],
                "answer": 1,
                "hint": "Pagtatakda ng malinaw na layunin."
            }
        ]
    },
    "mk-digital": {
        "title": "Aralin 3: Digital Identity at Netiquette",
        "lessonId": "lesson-mk-digital",
        "questions": [
            {
                "q": "Alin ang halimbawa ng PASSIVE digital footprint?",
                "options": ["Pag-upload ng video sa TikTok", "Pag-post ng litrato sa Instagram", "Web cookies at browsing history", "Pagkomento sa Facebook"],
                "answer": 2,
                "hint": "Awtomatikong nakokolekta nang hindi mo kusang pinopost."
            },
            {
                "q": "Ano ang tawag sa wastong asal at pag-uugali habang gumagamit ng internet?",
                "options": ["Digital Footprint", "Netiquette (Online Etiquette)", "Two-Factor Auth", "Public Profile"],
                "answer": 1,
                "hint": "Net + Etiquette = Netiquette."
            },
            {
                "q": "Bakit mahalagang i-on ang 2FA (Two-Factor Authentication)?",
                "options": ["Para sa karagdagang proteksyon sa personal na datos", "Para bumilis ang internet", "Para dumami ang likes", "Para maging public ang account"],
                "answer": 0,
                "hint": "Pangalagaan ang password at account security."
            }
        ]
    },
    "mk-proseso": {
        "title": "Aralin 4: 3 Proseso ng Komunikasyon",
        "lessonId": "lesson-mk-proseso",
        "questions": [
            {
                "q": "Alin sa 3 proseso ang tumutukoy sa pag-unawa at pagbibigay-kahulugan sa mensahe?",
                "options": ["Pagpapahayag (Expression)", "Pakikilahok (Participation)", "Pagbibigay-kahulugan (Decoding)", "Konteksto"],
                "answer": 2,
                "hint": "Apektado ito ng sariling karanasan at emosyon."
            },
            {
                "q": "Ang pakikilahok (participation) ay kinabibilangan ng:",
                "options": ["Pagsasalita lamang", "Aktibong pakikinig at pakikiisa sa talakayan", "Tahimik na pag-alis", "Pang-iinsulto sa kausap"],
                "answer": 1,
                "hint": "Kasama ang buong atensyon at paggalang."
            },
            {
                "q": "Ang galaw ng katawan, kumpas, at ekspresyon ng mukha ay anyo ng:",
                "options": ["Pagpapahayag (Expression)", "Hadlang", "Passive data", "2FA"],
                "answer": 0,
                "hint": "Di-berbal na paraan ng pagpapahayag."
            }
        ]
    },
    "mk-kultural": {
        "title": "Aralin 4: Kamalayang Kultural at Sensibilidad",
        "lessonId": "lesson-mk-kultural",
        "questions": [
            {
                "q": "Ano ang Kamalayang Kultural (Cultural Awareness)?",
                "options": ["Pilitin ang iba na gayahin ang iyong wika", "Pag-unawa at paggalang na magkakaiba ang kultura at tradisyon", "Pag-iwas sa pakikipag-usap sa banyaga", "Panghuhusga sa hindi nagpo-po at opo"],
                "answer": 1,
                "hint": "Pagkilala sa pagkakaiba ng mga kultura."
            },
            {
                "q": "Aling pahayag ang nagpapakita ng SENSIBILIDAD sa komunikasyon?",
                "options": ["'Maling-mali ka!'", "'Wala kang alam!'", "'Mayroon akong ibang pananaw ukol diyan.'", "'Tumahimik ka na lang.'"],
                "answer": 2,
                "hint": "Isinasaalang-alang ang mararamdaman ng kausap."
            },
            {
                "q": "Alin ang halimbawa ng 'Hadlang o Noise' sa komunikasyon?",
                "options": ["Maingay na paligid at mahinang signal", "Matinding galit o labis na emosyon", "Maling interpretasyon ng salita", "Lahat ng nabanggit"],
                "answer": 3,
                "hint": "Lahat ng nakasisira sa linaw ng usapan ay noise."
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
                "hint": "3rd = Effort in middle (e.g. fishing rod, broom)."
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
                "q": "Two inclined planes placed back-to-back used for cutting or splitting describe a:",
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
                "q": "How is the total MA of a compound machine calculated from its components?",
                "options": ["MA_total = MA1 + MA2", "MA_total = MA1 x MA2 x MA3...", "MA_total = (MA1 + MA2) / 2", "MA_total = MA1 - MA2"],
                "answer": 1,
                "hint": "Component mechanical advantages are multiplied together."
            },
            {
                "q": "Why are compound machines generally LESS efficient than single simple machines?",
                "options": ["They produce too much work", "More moving parts introduce more friction and heat loss", "They violate physics", "They have MA < 1"],
                "answer": 1,
                "hint": "More joints and surfaces create friction."
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
                "hint": "P1 = P2 throughout the enclosed fluid."
            },
            {
                "q": "In a hydraulic lift, if Piston 2 has 10 times the area of Piston 1, the output force F2 will be:",
                "options": ["10 times greater than F1", "10 times smaller than F1", "Equal to F1", "Zero"],
                "answer": 0,
                "hint": "F2 = F1 x (A2 / A1)."
            },
            {
                "q": "Which real-world machine operates directly on Pascal's Principle?",
                "options": ["Hydraulic car brakes and lifts", "A simple crowbar", "A fixed flagpole pulley", "A compass"],
                "answer": 0,
                "hint": "Hydraulic systems use fluid pressure transmission."
            }
        ]
    },
    "gs-archimedes": {
        "title": "Week 6: Archimedes' Principle & Buoyancy",
        "lessonId": "lesson-gs-archimedes",
        "questions": [
            {
                "q": "According to Archimedes' Principle, the Buoyant Force (Fb) on an object equals:",
                "options": ["The total weight of the object", "The weight of the fluid displaced by the object", "The depth of the water", "Zero in seawater"],
                "answer": 1,
                "hint": "Fb = Weight of displaced fluid."
            },
            {
                "q": "An object will SINK in water if:",
                "options": ["Its density is greater than water (Fb < Weight)", "Its density is less than water", "It is made of wood", "Its volume is large"],
                "answer": 0,
                "hint": "Gravity overcomes buoyant force when density is higher."
            },
            {
                "q": "Why do massive steel ships float on water?",
                "options": ["Steel is lighter than water", "The hollow hull displaces a large volume of water, creating large buoyant force", "Salt in the ocean repels steel", "Engines push the ship up"],
                "answer": 1,
                "hint": "High displaced volume creates huge upward buoyant force."
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
                "hint": "Mark-up = Selling Price - Cost Price (550 - 400 = 150)."
            },
            {
                "q": "A shoes pair originally priced at ₱1,000 is on a 25% discount. What is the Sale Price?",
                "options": ["₱250", "₱750", "₱1,250", "₱800"],
                "answer": 1,
                "hint": "Discount = 250. Sale Price = 1,000 - 250 = 750."
            },
            {
                "q": "What is the formula for Mark-up Rate based on Cost?",
                "options": ["(Mark-up / Cost) x 100%", "(Cost / Mark-up) x 100%", "Cost x Selling Price", "Selling Price - Discount"],
                "answer": 0,
                "hint": "Fraction of mark-up over original cost."
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
                "hint": "I = Prt where rate is decimal and time is in years."
            },
            {
                "q": "If you invest ₱20,000 at 4% annual simple interest for 2 years, how much interest is earned?",
                "options": ["₱800", "₱1,600", "₱21,600", "₱4,000"],
                "answer": 1,
                "hint": "I = 20,000 x 0.04 x 2 = 1,600."
            },
            {
                "q": "What is the Maturity Value (Future Value F) of the ₱20,000 investment above?",
                "options": ["₱1,600", "₱20,000", "₱21,600", "₱24,000"],
                "answer": 2,
                "hint": "F = Principal + Interest (20,000 + 1,600 = 21,600)."
            }
        ]
    },
    "gm-patterns": {
        "title": "Week 7: Patterns in Nature & Fibonacci",
        "lessonId": "lesson-gm-patterns",
        "questions": [
            {
                "q": "What are the next two terms in the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, __, __?",
                "options": ["10, 12", "13, 21", "11, 15", "16, 24"],
                "answer": 1,
                "hint": "5 + 8 = 13, and 8 + 13 = 21."
            },
            {
                "q": "Which type of symmetry is exhibited by a starfish and sunflower florets?",
                "options": ["Bilateral symmetry", "Radial / Rotational symmetry", "Asymmetry", "Translation"],
                "answer": 1,
                "hint": "Rotational symmetry around a central point."
            },
            {
                "q": "Why do honeybees build hexagonal honeycomb cells?",
                "options": ["Hexagons are random", "Hexagons maximize storage volume using minimal perimeter/wax", "To trap heat only", "Hexagons are easier to count"],
                "answer": 1,
                "hint": "Optimal geometric packing efficiency."
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
                "hint": "Add (n-1) differences to the initial term."
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
                "options": ["A 3D sculpture", "Covering a plane with geometric shapes without overlaps or gaps", "A mathematical equation", "A fractal dimension"],
                "answer": 1,
                "hint": "No gaps, no overlaps on a 2D surface."
            },
            {
                "q": "How many distinct Frieze Symmetry Groups exist in 1D border patterns?",
                "options": ["4", "7", "12", "17"],
                "answer": 1,
                "hint": "Exactly 7 frieze groups classify all repeating bands."
            },
            {
                "q": "Which transformation involves sliding an object along a straight line without rotation?",
                "options": ["Reflection", "Rotation", "Translation", "Glide Reflection"],
                "answer": 2,
                "hint": "Pure linear shift is Translation."
            }
        ]
    },
    "fn-golden": {
        "title": "Lesson 4: Golden Ratio & Fibonacci Spirals",
        "lessonId": "lesson-fn-golden",
        "questions": [
            {
                "q": "What is the approximate numerical value of the Golden Ratio (Phi, φ)?",
                "options": ["3.1416", "1.618", "2.718", "1.414"],
                "answer": 1,
                "hint": "φ = (1 + √5) / 2 ≈ 1.6180339887."
            },
            {
                "q": "A Golden Rectangle has side lengths in the ratio:",
                "options": ["2 : 1", "1.618 : 1 (φ : 1)", "3 : 2", "1 : 1"],
                "answer": 1,
                "hint": "Length / Width = φ."
            },
            {
                "q": "As the Fibonacci sequence progresses, the ratio of consecutive terms (Fn+1 / Fn) approaches:",
                "options": ["0", "1", "The Golden Ratio (φ ≈ 1.618)", "Infinity"],
                "answer": 2,
                "hint": "Fibonacci ratios converge to the Golden Ratio."
            }
        ]
    },
    "fn-fractals": {
        "title": "Lesson 5: Fractals & Self-Similarity",
        "lessonId": "lesson-fn-fractals",
        "questions": [
            {
                "q": "What is the defining property of a Fractal (such as the Sierpinski Triangle)?",
                "options": ["Straight lines only", "Self-Similarity (repeats structure at every magnification scale)", "Fixed area and zero perimeter", "Finite iterations only"],
                "answer": 1,
                "hint": "Zooming in reveals identical smaller copies of the whole pattern."
            },
            {
                "q": "Which of the following is a classic mathematical fractal?",
                "options": ["Sierpinski Gasket / Triangle", "Koch Snowflake", "Mandelbrot Set", "All of the above"],
                "answer": 3,
                "hint": "All three are prominent fractals."
            },
            {
                "q": "Which natural phenomenon displays fractal geometry?",
                "options": ["Fern leaves and coastlines", "Lightning branches and river networks", "Blood vessels and lung bronchi", "All of the above"],
                "answer": 3,
                "hint": "Nature frequently employs fractal branching."
            }
        ]
    },
    "fn-matrix": {
        "title": "Lessons 6 & 7: Matrix Algebra & Multiplication",
        "lessonId": "lesson-fn-matrix",
        "questions": [
            {
                "q": "To ADD two matrices, they must have:",
                "options": ["The same number of rows as columns", "Identical dimensions (same number of rows and columns)", "Determinants equal to 1", "Only positive entries"],
                "answer": 1,
                "hint": "Addition requires equal dimensions (m x n)."
            },
            {
                "q": "What condition must be met to MULTIPLY Matrix A (m x k) and Matrix B (p x n)?",
                "options": ["Columns of A (k) must equal Rows of B (p)", "Rows of A must equal Rows of B", "Both must be square", "k must equal m"],
                "answer": 0,
                "hint": "Inner dimensions must match: (m x k) • (k x n) = (m x n)."
            },
            {
                "q": "If Matrix A is of order (2 x 3) and Matrix B is (3 x 4), what is the order of the product AB?",
                "options": ["2 x 4", "3 x 3", "2 x 3", "Undefined"],
                "answer": 0,
                "hint": "Outer dimensions form the product: (2 x 3) • (3 x 4) = (2 x 4)."
            }
        ]
    }
}

print(f"Loaded {len(ALL_LESSON_QUIZZES)} distinct lesson quizzes into the database!")
