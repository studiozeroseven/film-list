import media
import fresh_tomatoes

# I pulled this from the class and am using it here, I know there is a better way of doing this  # noqa
# Test comment

VALID_RATINGS = ["G", "PG", "PG-13", "R"]

toy_story = media.Movie("Toy Story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who \
                        belongs to a young boy named Andy (John Morris), sees \
                        his position as Andy's favorite toy jeopardized when \
                        his parents buy him a Buzz Lightyear (Tim Allen) \
                        action figure",
                        "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",  # noqa
                        "https://www.youtube.com/watch?v=4KPTXpQehio",
                        VALID_RATINGS[0])

fight_club = media.Movie("Fight Club",
                         "A depressed man (Edward Norton) suffering from \
                         insomnia meets a strange soap salesman named Tyler \
                         Durden (Brad Pitt) and soon finds himself living in \
                         his squalid house after his perfect apartment is \
                         destroyed. The two bored men form an underground \
                         club with strict rules and fight other men who are \
                         fed up with their mundane lives.",
                         "http://www.gstatic.com/tv/thumb/movieposters/23069/p23069_p_v8_ad.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         VALID_RATINGS[3])

ratatouille = media.Movie("Ratatouille",
                          "Remy (Patton Oswalt), a resident of Paris, \
                          appreciates good food and has quite a sophisticated \
                          palate. He would love to become a chef so he can \
                          create and enjoy culinary masterpieces to his \
                          heart's delight. The only problem is, Remy is a \
                          rat. When he winds up in the sewer beneath one of \
                          Paris' finest restaurants, the rodent gourmet finds \
                          himself ideally placed to realize his dream.",
                          "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",  # noqa
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          VALID_RATINGS[0])

cars3 = media.Movie("Cars 3",
                    "Blindsided by a new generation of blazing-fast cars, the \
                    legendary Lighting McQueen finds himself pushed out of \
                    the sport that he loves. Hoping to get back in the game, \
                    he turns to Cruz Ramirez, an eager young technician who \
                    has her own plans for winning. With inspiration from the \
                    Fabulous Hudson Hornet and a few unexpected turns, No. 95 \
                    prepares to compete on Piston Cup Racing's biggest stage.",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcScCXoxJL2rdif-y-lYk_H0jgH_eyFrAXk7yfpUW43xpLW8AmHk",  # noqa
                    "https://www.youtube.com/watch?v=2LeOH9AGJQM",
                    VALID_RATINGS[0])

wonder_woman = media.Movie("Wonder Woman",
                           "Before she was Wonder Woman (Gal Gadot), she was \
                           Diana, princess of the Amazons, trained to be an \
                           unconquerable warrior. Raised on a sheltered \
                           island paradise, Diana meets an American pilot \
                           (Chris Pine) who tells her about the massive \
                           conflict that's raging in the outside world. \
                           Convinced that she can stop the threat, Diana \
                           leaves her home for the first time.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",  # noqa
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
                           VALID_RATINGS[2])

avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na'vi, \
                     beings who appear primitive but are highly evolved. \
                     Because the planet's environment is poisonous, \
                     human/Na'vi hybrids, called Avatars, must link to human \
                     minds to allow for free movement on Pandora. Jake Sully \
                     (Sam Worthington), a paralyzed former Marine, becomes \
                     mobile again through one such Avatar and falls in love \
                     with a Na'vi woman (Zoe Saldana).",
                     "http://1.bp.blogspot.com/_DIxqmRCvMcI/SzOZ9v_d3CI/AAAAAAAAABc/oFSooZ2lkOU/w1200-h630-p-k-no-nu/avatar_movie_James%2BCameron%E2%80%99s_Hollywood%2Bmovie.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     VALID_RATINGS[2])

movies = [toy_story, fight_club, ratatouille, cars3, wonder_woman, avatar]
fresh_tomatoes.open_movies_page(movies)
