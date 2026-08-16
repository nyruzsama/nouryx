import os
import json

# Define the complete quiz data for every lesson across all 4 subjects
QUIZ_DATA = {
    # 1. MabKom Lesson 1 (Aralin 3: Pagpapahayag, Elemento, Intrapersonal, Netiquette)
    "mk-a3": {
        "title": "Aralin 3: Malinaw na Pagpapahayag at Netiquette",
        "questions": [
            {
                "q": "Ano ang tawag sa elemento ng komunikasyon na nagbibigay ng reaksyon o sagot sa mensahe?",
                "options": ["Daluyan (Channel)", "Tugon (Feedback)", "Tagapagpadala (Sender)", "Hadlang (Noise)"],
                "answer": 1,
                "hint": "Ito ang nagpapatunay kung naunawaan ang mensahe."
            },
            {
                "q": "Alin sa mga sumusunod ang halimbawa ng PASSIVE digital footprint?",
                "options": ["Pag-post ng selfie sa Instagram", "Pagkomento sa Facebook post", "Web cookies at browsing history", "Pag-send ng chat sa Messenger"],
                "answer": 2,
                "hint": "Awtomatikong nakokolekta nang hindi mo kusang pinopost."
            },
            {
                "q": "Anong anyo ng intrapersonal na komunikasyon ang mas SISTEMATIKONG talaan ng mga natutuhan at obserbasyon?",
                "options": ["Dyornal (Journal)", "Talaarawan (Diary)", "Advocacy Post", "Komentaryo"],
                "answer": 0,
                "hint": "Mas nakatutok sa aral at obserbasyon kaysa sa simpleng diary."
            },
            {
                "q": "Bakit mahalagang i-on ang 2FA (Two-Factor Authentication)?",
                "options": ["Para dumami ang followers", "Proteksyon sa personal na datos at account security", "Para bumilis ang internet", "Para maging active ang footprint"],
                "answer": 1,
                "hint": "Karagdagang layer ng seguridad laban sa mga hacker."
            },
            {
                "q": "Ang pagpapahayag ng obserbasyon ay dapat gawin nang:",
                "options": ["May kasamang galit", "Hindi agad nagbibigay ng sariling paghuhusga", "Gamit ang all caps", "Sa pamamagitan lamang ng diary"],
                "answer": 1,
                "hint": "Naglalahad ng nakita o narinig nang walang agarang paninisi."
            }
        ]
    },

    # 2. MabKom Lesson 2 (Aralin 4: Proseso, Konteksto, Kamalayang Kultural)
    "mk-a4": {
        "title": "Aralin 4: Proseso at Kamalayang Kultural",
        "questions": [
            {
                "q": "Alin sa 3 proseso ng komunikasyon ang tumutukoy sa pag-unawa at pagbibigay-kahulugan sa mensahe?",
                "options": ["Pagpapahayag (Expression)", "Pakikilahok (Participation)", "Pagbibigay-kahulugan (Decoding)", "Konteksto (Context)"],
                "answer": 2,
                "hint": "Nakaaapekto rito ang karanasan at emosyon."
            },
            {
                "q": "Kapag sinabi ng nanay 'Umuwi ka nang maaga', ano ang maaaring malalim na pahiwatig nito?",
                "options": ["Nais lamang siyang pagalitan", "Nag-aalala sa kaniyang kaligtasan", "Wala lang", "Nais maglinis ng bahay"],
                "answer": 1,
                "hint": "Ang komunikasyon ay bumubuo ng relasyon at nagpapahayag ng damdamin."
            },
            {
                "q": "Alin ang nagpapakita ng SENSIBILIDAD sa komunikasyon?",
                "options": ["'Maling-mali ka!'", "'Wala kang alam!'", "'Mayroon akong ibang pananaw ukol diyan.'", "'Manahimik ka na lang.'"],
                "answer": 2,
                "hint": "Isinasaalang-alang ang damdamin ng kausap."
            },
            {
                "q": "Bakit normal ang 'po' at 'opo' sa Pilipinas pero hindi sa ibang bansa?",
                "options": ["Dahil bastos ang ibang bansa", "Dahil sa pagkakaiba ng kulturang kinagisnan (Kamalayang Kultural)", "Dahil bawal mag-po sa ibang bansa", "Dahil mali ang balarila nila"],
                "answer": 1,
                "hint": "Paggalang sa pagkakaiba-iba ng kultura at tradisyon."
            },
            {
                "q": "Alin ang maituturing na 'Hadlang o Noise' sa komunikasyon?",
                "options": ["Maingay na paligid at mahinang signal", "Matinding galit at emosyon", "Maling interpretasyon ng salita", "Lahat ng nabanggit"],
                "answer": 3,
                "hint": "Lahat ng nakagagambala sa malinaw na usapan ay noise."
            }
        ]
    },

    # 3. Gen Science: Simple Machines (W5)
    "gs-w5simple": {
        "title": "Week 5: Simple Machines & Mechanical Advantage",
        "questions": [
            {
                "q": "Which class of lever has the LOAD in the middle (between fulcrum and effort)?",
                "options": ["1st Class Lever", "2nd Class Lever", "3rd Class Lever", "4th Class Lever"],
                "answer": 1,
                "hint": "Memory rule: 1st=F, 2nd=L, 3rd=E in the middle! Wheelbarrow is an example."
            },
            {
                "q": "What is the formula for the Mechanical Advantage (MA) of any machine?",
                "options": ["MA = Effort Force / Load Force", "MA = Load Force / Effort Force", "MA = Work x Distance", "MA = Height / Length"],
                "answer": 1,
                "hint": "Output force divided by Input force."
            },
            {
                "q": "A fixed pulley has a Mechanical Advantage of:",
                "options": ["0", "1 (only redirects force)", "2", "4"],
                "answer": 1,
                "hint": "It changes direction only, it does not multiply force."
            },
            {
                "q": "A ramp has a length of 12 m and height of 3 m. What is its Ideal Mechanical Advantage (IMA)?",
                "options": ["0.25", "4", "36", "9"],
                "answer": 1,
                "hint": "IMA of Inclined Plane = Length / Height (12 / 3 = 4)."
            },
            {
                "q": "Do simple machines reduce the TOTAL WORK done?",
                "options": ["Yes, by 50%", "No, total work remains the same (trade-off: less force, more distance)", "Yes, friction is eliminated", "Only for 2nd class levers"],
                "answer": 1,
                "hint": "Conservation of energy: Work In = Work Out (ignoring friction)."
            }
        ]
    },

    # 4. Gen Science: Compound Machines & Pascal / Archimedes (W6)
    "gs-w6pascal": {
        "title": "Week 6: Compound Machines, Pascal's & Archimedes' Principles",
        "questions": [
            {
                "q": "How is the total Mechanical Advantage (MA) of a compound machine calculated?",
                "options": ["MA_total = MA1 + MA2 + MA3", "MA_total = MA1 x MA2 x MA3...", "MA_total = (MA1 + MA2) / 2", "MA_total = MA1 - MA2"],
                "answer": 1,
                "hint": "Component MAs are multiplied together!"
            },
            {
                "q": "Pascal's Principle states that pressure applied to an enclosed fluid is:",
                "options": ["Lost at the bottom", "Transmitted undiminished in all directions", "Decreased by half", "Only applied upwards"],
                "answer": 1,
                "hint": "F1/A1 = F2/A2 (Hydraulic lifts & brakes)."
            },
            {
                "q": "According to Archimedes' Principle, the Buoyant Force (Fb) on a submerged object equals:",
                "options": ["The total weight of the object", "The weight of the fluid displaced by the object", "The surface area of the container", "Zero in water"],
                "answer": 1,
                "hint": "Fb = Weight of displaced fluid."
            },
            {
                "q": "An object will FLOAT if its Buoyant Force (Fb) is:",
                "options": ["Less than its weight", "Equal to or greater than its weight (Density < fluid density)", "Zero", "Negative"],
                "answer": 1,
                "hint": "Floating occurs when upward buoyant force balances gravity."
            },
            {
                "q": "In a hydraulic lift, A1 = 2 cm² and A2 = 20 cm². If F1 = 50 N, what is F2?",
                "options": ["5 N", "50 N", "500 N", "100 N"],
                "answer": 2,
                "hint": "F2 = F1 x (A2/A1) = 50 x (20/2) = 500 N."
            }
        ]
    },

    # 5. Gen Math: Percentages & Business Math (W6)
    "gm-w6": {
        "title": "Week 6: Percentages in Business & Finance",
        "questions": [
            {
                "q": "What is the formula for Simple Interest (I)?",
                "options": ["I = P + r + t", "I = P x r x t (Principal x Rate x Time)", "I = P / (r x t)", "I = P(1 + r)^t"],
                "answer": 1,
                "hint": "I = Prt where rate is in decimal and time is in years."
            },
            {
                "q": "An item costs ₱500 and is sold for ₱650. What is the Mark-up amount?",
                "options": ["₱100", "₱150", "₱1,150", "₱300"],
                "answer": 1,
                "hint": "Mark-up = Selling Price - Cost Price (650 - 500 = 150)."
            },
            {
                "q": "A shirt priced at ₱800 has a 20% discount. What is the Sale Price?",
                "options": ["₱160", "₱640", "₱780", "₱600"],
                "answer": 1,
                "hint": "Discount = 800 x 0.20 = 160. Sale Price = 800 - 160 = 640."
            },
            {
                "q": "If you invest ₱10,000 at 5% simple annual interest for 3 years, how much interest is earned?",
                "options": ["₱500", "₱1,500", "₱15,000", "₱1,000"],
                "answer": 1,
                "hint": "I = 10,000 x 0.05 x 3 = 1,500."
            },
            {
                "q": "What does 'Principal' (P) refer to in loans and investments?",
                "options": ["The school head", "The original amount of money borrowed or invested", "The interest rate percentage", "The maturity date"],
                "answer": 1,
                "hint": "Initial sum before interest is added."
            }
        ]
    },

    # 6. Gen Math: Nature Patterns & Sequences (W7 & W8)
    "gm-w7w8": {
        "title": "Weeks 7 & 8: Patterns, Fibonacci & Sequences",
        "questions": [
            {
                "q": "What are the next two numbers in the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, __, __?",
                "options": ["10, 12", "13, 21", "11, 15", "16, 24"],
                "answer": 1,
                "hint": "Each term is the sum of the previous two (5+8=13, 8+13=21)."
            },
            {
                "q": "In the Arithmetic Sequence 3, 7, 11, 15..., what is the Common Difference (d)?",
                "options": ["2", "3", "4", "5"],
                "answer": 2,
                "hint": "d = 7 - 3 = 4."
            },
            {
                "q": "What is the formula for the nth term of an Arithmetic Sequence?",
                "options": ["an = a1 + (n - 1)d", "an = a1 x r^(n-1)", "an = n x d", "an = (a1 + an) / 2"],
                "answer": 0,
                "hint": "Start with first term a1 and add (n-1) differences."
            },
            {
                "q": "In the Geometric Sequence 2, 6, 18, 54..., what is the Common Ratio (r)?",
                "options": ["2", "3", "4", "6"],
                "answer": 1,
                "hint": "r = 6 / 2 = 3."
            },
            {
                "q": "What type of symmetry is exhibited by starfish and sunflowers?",
                "options": ["Bilateral symmetry", "Radial / Rotational symmetry", "No symmetry", "Glide reflection"],
                "answer": 1,
                "hint": "Symmetry around a central axis."
            }
        ]
    },

    # 7. Finite Math: Tessellations & Golden Ratio (Lessons 3 & 4)
    "fn-l3l4": {
        "title": "Lessons 3 & 4: Tessellations, Frieze & Golden Ratio",
        "questions": [
            {
                "q": "What is the approximate numerical value of the Golden Ratio (Phi, φ)?",
                "options": ["3.14159", "1.618", "2.718", "1.414"],
                "answer": 1,
                "hint": "φ = (1 + √5) / 2 ≈ 1.6180339887."
            },
            {
                "q": "How many distinct Frieze Groups (infinite 1D border patterns) exist in mathematics?",
                "options": ["4", "7", "12", "17"],
                "answer": 1,
                "hint": "Exactly 7 frieze symmetry groups classify all 1D repeated patterns."
            },
            {
                "q": "What is a Tessellation (or Tiling)?",
                "options": ["A 3D sculpture", "Covering a plane using geometric shapes without overlaps or gaps", "A spiral pattern in shells", "A matrix product"],
                "answer": 1,
                "hint": "No gaps, no overlaps on a flat 2D plane (like M.C. Escher art)."
            },
            {
                "q": "A Golden Rectangle has a length-to-width ratio equal to:",
                "options": ["2:1", "1.618 : 1 (φ : 1)", "3:2", "1:1"],
                "answer": 1,
                "hint": "Length / Width = φ ≈ 1.618."
            },
            {
                "q": "Which transformation involves sliding an object along a straight line without turning?",
                "options": ["Rotation", "Reflection", "Translation", "Glide Reflection"],
                "answer": 2,
                "hint": "Pure linear shift is Translation."
            }
        ]
    },

    # 8. Finite Math: Fractals & Matrix Operations (Lessons 5, 6 & 7)
    "fn-l5l6l7": {
        "title": "Lessons 5, 6 & 7: Fractals & Matrix Algebra",
        "questions": [
            {
                "q": "What is the key characteristic of a Fractal (like the Sierpinski Triangle)?",
                "options": ["Smooth straight edges", "Self-Similarity (repeating structure at every magnification scale)", "Fixed whole number dimensions only", "Zero perimeter"],
                "answer": 1,
                "hint": "Zooming in reveals identical smaller replicas of the whole pattern."
            },
            {
                "q": "What condition must be met to MULTIPLY Matrix A (order m x k) and Matrix B (order p x n)?",
                "options": ["They must have the exact same dimensions", "Columns of A (k) must equal Rows of B (p)", "Both must be square matrices", "k must equal m"],
                "answer": 1,
                "hint": "Inner dimensions must match: (m x k) • (k x n) = (m x n)."
            },
            {
                "q": "If Matrix A is of size (2 x 3) and Matrix B is of size (3 x 4), what is the size of the product AB?",
                "options": ["2 x 4", "3 x 3", "2 x 3", "Undefined / Cannot multiply"],
                "answer": 0,
                "hint": "Outer dimensions form the result: (2 x 3) • (3 x 4) = (2 x 4)."
            },
            {
                "q": "To ADD two matrices, they must have:",
                "options": ["The same number of rows as columns", "Identical dimensions (same number of rows and columns)", "Determinants equal to 1", "Only positive numbers"],
                "answer": 1,
                "hint": "Element-by-element addition requires identical orders (m x n)."
            },
            {
                "q": "If scalar k = 3 is multiplied with a matrix, how is each element calculated?",
                "options": ["Only the first element is multiplied by 3", "Every single entry in the matrix is multiplied by 3", "3 is added to every entry", "The matrix is transposed"],
                "answer": 1,
                "hint": "Scalar multiplication scales every element by k."
            }
        ]
    }
}

print("Loaded Quiz Database with", len(QUIZ_DATA), "interactive lesson quiz modules!")
