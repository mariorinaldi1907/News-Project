from flask import Flask, render_template, abort

app = Flask(__name__)

articles = {
    "underground-space-costs": {
        "title": "Singapore maps deeper underground routes to reduce future building delays",
        "category": "Singapore",
        "date": "14 June 2026",
        "author": "Rachel Tan",
        "caption": "Urban planners say better underground mapping can help major projects avoid costly surprises.",
        "summary": "New digital surveys are helping engineers plan tunnels, utilities and transport links with fewer disruptions.",
        "featured": True,
        "content": [
            "Singapore is expanding the use of digital underground mapping as agencies and builders prepare for another wave of transport, utilities and public housing projects. Planners say clearer information about pipes, cables and soil conditions can reduce delays before construction begins.",
            "The work is especially important in dense estates where rail lines, drainage networks and utility corridors often sit close together. Engineers say early mapping gives project teams more confidence when deciding where to place tunnels, foundations and service routes.",
            "Industry observers believe the approach could help keep costs stable, although they caution that digital tools cannot remove every risk. Unexpected ground conditions, weather and supply delays may still affect timelines.",
            "Residents may notice more survey work in selected areas, but officials say most of the process will be carried out with limited disruption. The aim is to make construction planning less reactive and more predictable.",
            "Analysts say Singapore's long-term challenge is not only building more infrastructure, but doing so while keeping neighbourhoods liveable during works. Better information, they add, is becoming as important as machinery on the ground."
        ]
    },
    "resale-condos-market": {
        "title": "Resale condos stay on the market longer as buyers take more time",
        "category": "Business",
        "date": "13 June 2026",
        "author": "Darren Koh",
        "caption": "Some private home buyers are comparing more listings before making offers.",
        "summary": "Property agents say buyers remain interested, but many are more cautious about price and loan commitments.",
        "content": [
            "Private resale homes are taking longer to move in several districts as buyers weigh higher living costs and financing commitments. Agents say viewings remain steady, but offers are becoming more selective.",
            "Sellers who priced their units aggressively earlier in the year are now facing more negotiation. Some have chosen to wait rather than cut asking prices, especially in areas with limited supply.",
            "Market watchers say the slowdown does not point to a sharp correction. Instead, they describe it as a more balanced market where buyers want clearer value before committing.",
            "Younger households are also comparing resale units with new launches, public housing options and rental choices. This has made decision-making slower, even among serious buyers.",
            "Analysts expect demand to remain supported by employment stability, but say affordability will continue to shape the pace of transactions."
        ]
    },
    "ev-driving-rules": {
        "title": "Updated driving rules widen access to heavier electric vehicles",
        "category": "Singapore",
        "date": "12 June 2026",
        "author": "Hannah Lee",
        "caption": "Electric vans and small buses can be heavier because of battery packs.",
        "summary": "The update is expected to help firms adopt cleaner fleets while keeping safety checks in place.",
        "content": [
            "More drivers will be allowed to operate selected electric vehicles under updated licensing rules that recognise the extra weight of battery systems. Transport firms say the change could support cleaner commercial fleets.",
            "Electric vans often weigh more than petrol or diesel models of similar size. Without rule changes, some drivers would need a different licence even when the vehicle serves the same business purpose.",
            "The authorities are expected to keep safety requirements, including training and vehicle checks, as heavier vehicles can behave differently on the road.",
            "Logistics operators say the move gives them more confidence to plan fleet replacement. However, charging access and vehicle cost remain important concerns.",
            "Environmental groups welcomed the update, saying practical rules are needed if Singapore wants transport emissions to fall without slowing daily business operations."
        ]
    },
    "f1-singapore-night-race": {
        "title": "Singapore Grand Prix organisers prepare brighter fan zones for night race weekend",
        "category": "Sport",
        "date": "11 June 2026",
        "author": "Marcus Neo",
        "caption": "The Marina Bay street race remains one of Singapore's biggest international sporting weekends.",
        "summary": "New crowd-flow plans and expanded viewing areas are being prepared for the Formula 1 Singapore Grand Prix.",
        "content": [
            "Organisers of the Formula 1 Singapore Grand Prix are preparing upgraded fan zones, clearer walking routes and more food areas around the Marina Bay street circuit as the city gets ready for another night race weekend.",
            "The event is expected to draw local fans, regional visitors and corporate guests, giving hotels, restaurants and retailers a busy stretch. Businesses near the circuit say the race brings strong footfall, although road closures require careful planning.",
            "Motorsport fans will be watching how teams handle the humid conditions and tight corners that make Singapore one of the most demanding races on the calendar. Strategy, tyre management and safety car timing often play a major role.",
            "Tourism analysts say the race is valuable because it presents Singapore as both a business city and an entertainment destination. The night skyline, concerts and street circuit create a distinctive image for international audiences.",
            "Organisers say crowd safety will remain a priority, with more signs and transport reminders planned for visitors moving between MRT stations, gates and viewing areas."
        ]
    },
    "asean-supply-chains": {
        "title": "ASEAN firms look to Singapore as supply chains become more regional",
        "category": "World",
        "date": "10 June 2026",
        "author": "Nadia Rahman",
        "caption": "Regional businesses are reviewing logistics routes and warehousing needs.",
        "summary": "Companies are using Singapore for finance, legal support and coordination as manufacturing spreads across the region.",
        "content": [
            "Companies across Southeast Asia are reviewing supply chains as they seek to reduce delays and build more resilient regional networks. Singapore is being used by many firms as a coordination base rather than a manufacturing centre.",
            "Executives say the city remains useful for finance, insurance, legal services and logistics planning. These functions are becoming more important as production is spread across several countries.",
            "Analysts note that regionalisation does not mean global trade is disappearing. Instead, companies want more options when shipping routes, tariffs or geopolitical tensions create uncertainty.",
            "Small and medium-sized firms may benefit from shared warehousing and digital trade platforms, although costs remain a concern.",
            "Economists say Singapore's role will depend on how quickly it can help businesses move goods, data and money across borders with minimal friction."
        ]
    },
    "ai-classrooms": {
        "title": "Schools test AI tools for marking practice essays and planning lessons",
        "category": "Tech",
        "date": "9 June 2026",
        "author": "Joel Wong",
        "caption": "Teachers say AI tools can save time, but classroom judgement remains essential.",
        "summary": "Pilot projects are exploring how artificial intelligence can support teachers without replacing feedback from educators.",
        "content": [
            "Several schools are experimenting with artificial intelligence tools that help teachers review practice essays, prepare lesson outlines and generate quiz questions. Educators say the technology is useful when treated as an assistant rather than an authority.",
            "Teachers involved in early trials say AI can highlight grammar issues and suggest areas for improvement, but it may miss context, tone or creativity. Students are being reminded to check suggestions carefully.",
            "Parents have raised questions about privacy and fairness. Schools say safeguards are needed before any tool is used widely, especially when student work is involved.",
            "Education specialists believe AI literacy should become part of digital skills. They say students need to understand both the strengths and limits of automated systems.",
            "For now, teachers say the biggest benefit is time saved on routine preparation, allowing more attention to be given to classroom discussion and individual support."
        ]
    },
    "opinion-green-city": {
        "title": "Opinion: A greener city must still feel convenient for everyday life",
        "category": "Opinion",
        "date": "8 June 2026",
        "author": "Mei Lin",
        "caption": "Green planning works best when it supports daily routines.",
        "summary": "Sustainability policies gain support when residents can see practical benefits in transport, housing and neighbourhood design.",
        "content": [
            "Singapore's green goals will be judged not only by targets, but by how they feel in daily life. Residents are more likely to support change when cleaner choices are also convenient choices.",
            "Cycling paths, shaded walkways and reliable public transport can reduce car dependence, but they must connect to places people actually visit. A beautiful path that ends awkwardly will not change many habits.",
            "Housing estates also matter. More trees, cooler common areas and better waste systems can make sustainability visible at home, not just in national campaigns.",
            "The challenge is to avoid treating green policy as a lecture. People respond better when they experience comfort, savings and healthier surroundings.",
            "A greener city should not feel like a sacrifice. It should feel like a better version of the city residents already know."
        ]
    }
}

latest_headlines = [
    {"time": "12 mins ago", "headline": "Critics circle after late drama in major football qualifier"},
    {"time": "18 mins ago", "headline": "Police appeal for information after teenager reported missing in Jurong West"},
    {"time": "39 mins ago", "headline": "Asian markets mixed as investors await central bank signals"},
    {"time": "55 mins ago", "headline": "New community health pilot to open in three heartland towns"},
    {"time": "1 hour ago", "headline": "Regional leaders call for faster action on digital trade rules"},
]

@app.route("/")
def home():
    article_list = list(articles.items())
    hero_slug, hero_article = next((slug, article) for slug, article in article_list if article.get("featured"))
    secondary_articles = [(slug, article) for slug, article in article_list if slug != hero_slug]

    # Category order used by the navigation links and homepage sections
    categories = ["Singapore", "Business", "World", "Sport", "Tech", "Opinion"]
    category_sections = {}

    for category in categories:
        category_sections[category] = [
            (slug, article)
            for slug, article in article_list
            if article["category"] == category
        ]

    return render_template(
        "index.html",
        hero_slug=hero_slug,
        hero_article=hero_article,
        articles=secondary_articles,
        latest_headlines=latest_headlines,
        categories=categories,
        category_sections=category_sections,
    )

@app.route("/article/<slug>")
def article_page(slug):
    article = articles.get(slug)
    if article is None:
        abort(404)

    related = [(s, a) for s, a in articles.items() if s != slug and a["category"] == article["category"]]
    if len(related) < 3:
        related += [(s, a) for s, a in articles.items() if s != slug and (s, a) not in related]

    return render_template("article.html", article=article, related=related[:3])

if __name__ == "__main__":
    app.run(debug=True)
