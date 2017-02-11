START_TEXT = "Hi, and welcome to the Curious Minds Podcast chatbot. Please select one of the buttons below to continue."

class EpisodeInfo(object):

    def __init__(self, name, ep_url, mp3_url, transcript_url, description, image_url, topic, id):

        self.name = name
        self.ep_url  = ep_url
        self.mp3_url = mp3_url
        self.transcript_url = transcript_url
        self.description = description
        self.image_url = image_url
        self.topic = topic
        self.id = id


ep_software_bugs_part1 = EpisodeInfo(
                            "Are Software Bugs Inevitable? Part I",
                            "http://www.cmpod.net/are-software-bugs-inevitable-part-1-fortran-and-the-denver-airport-baggage-disaster-curious-minds-podcast/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/ycxzpm/CM_Software_Crisis_Part1.mp3",
                            "http://www.cmpod.net/are-software-bugs-inevitable-part-1-fortran-and-the-denver-airport-baggage-disaster-curious-minds-podcast/#text",
                            "Software errors and random bugs are rather common: We’ve all seen the infamous Windows “blue screen of death”… But is there really nothing we can do about it? Are these errors – from small bugs to catastrophic mistakes – inevitable?",
                            "http://www.cmpod.net/wp-content/uploads/2017/01/Software-560x270.png",
                            "Tech.",
                            "00")

ep_file_sharing_part1 = EpisodeInfo(
                            "The History of File Sharing Part I",
                            "http://www.cmpod.net/the-history-of-file-sharing-part-1-of-2-the-rise-fall-of-napster-curious-minds-podcast/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/ndb97f/CM_FileSharingPart1.mp3",
                            "http://www.cmpod.net/all-transcripts/history-file-sharing-part-1-2-rise-fall-napster_text/",
                            "Napster, a revolutionary Peer-to-Peer file sharing software, was launched in 1999 – and forever changed the media world. In this episode, we’ll tell the story of Sean Fanning and Sean Parker, its creators, and talk about the legal battle it fought with the record companies – and Metallica.",
                            "http://www.cmpod.net/wp-content/uploads/2016/11/FileSharing1-604x270.jpg",
                            "Tech.",
                            "01")

ep_indo_european_part1 = EpisodeInfo(
                            "The Indo-European Language Part I",
                            "http://www.cmpod.net/ancient-indo-european-language-pt-1/",
                            "https://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/92ycbc/CM_Indo_European_Pt_1.mp3",
                            "http://www.cmpod.net/all-transcripts/ancient-indo-european-language-text/",
                            "William Jones, a British judge in India, uncovered the existence of an ancient language, the ancestor of an amazing variety of modern languages – from English and French to the Persian Farsi and Indian Sanskrit.",
                            "http://www.cmpod.net/wp-content/uploads/2016/04/Sir_William_Jones-250x300.jpg",
                            "Humanities",
                            "02")

ep_uboats_part1 = EpisodeInfo(
                            "U-Boats Technology in WWII Part I",
                            "http://www.cmpod.net/uboats_in_wwii_part1/",
                            "https://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/rkit8d/CM_Uboats_Part1.mp3",
                            "http://www.cmpod.net/all-transcripts/wolf-packs-and-floating-coffins-u-boats-in-wwii-text/",
                            "How did the small, outgunned German fleet manage to strike painful blows to the Great British Navy in WW2? The credit for this success belongs to the German flotilla of submarines: the Unterseeboots, or U-Boats.",
                            "http://www.cmpod.net/wp-content/uploads/2015/09/U-25-150x150.jpg",
                            "Humanities",
                            "03")

ep_opensource_part1 = EpisodeInfo(
                            "The History of Open Source & Free Software Part I",
                            "http://www.cmpod.net/history_of_open_source_pt1/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/96xany/CM_FreeSoftware_Pt1.mp3",
                            "http://www.cmpod.net/all-transcripts/history-open-source-free-software-text/",
                            "In the early 1980’s Richard Stallman founded the Free Software Foundation (FSF): a socio-technological movement that revolutionized the software world. In this episode, we’ll hear Stallman himself talking about the roots of the movement, and learn of its early struggles.",
                            "http://www.cmpod.net/wp-content/uploads/2016/06/Richard_Matthew_Stallman-150x150.jpeg",
                            "Tech",
                            "04")

ep_stuxnet_part1 = EpisodeInfo(
                            "Stuxnet: The Malware That Struck Iran’s Nuclear Program Part I",
                            "http://www.cmpod.net/stuxnet-the-malware-that-struck-the-iranian-nuclear-program-pt-1/",
                            "https://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/qzbpny/CMPod_Stuxnet_Pt1.mp3",
                            "http://www.cmpod.net/all-transcripts/stuxnet-the-malware-that-struck-the-iranian-nuclear-program-text/",
                            "A special 3-parts series exploring the first cyber-weapon in-depth, including its target, creators, and implications on cyber security.",
                            "http://www.cmpod.net/wp-content/uploads/2016/02/iran-nuclear-program-150x150.jpg",
                            "Tech",
                            "05")

ep_preservation_part1 = EpisodeInfo(
                            "Digital Preservation & The Domesday Project",
                            "http://www.cmpod.net/digital-information-preservation/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/uyqaws/CM_Info_Preservation_Final.mp3",
                            "http://www.cmpod.net/all-transcripts/a-domesday-failure-digital-info-preservation-text/",
                            "In the 1980’s, the British BBC invested millions of pounds on what should have been a technological marvel: a modern version of the famous medieval Domesday Book. Less then 15 years later, it’s system was unusable. Compare that expensive failure to the longevity of the Domesday Book: a record written on paper in Latin in the 11th century and is still readable today. What can these two case studies tell us about the challenges and potential solutions to Digital Preservation?",
                            "http://www.cmpod.net/wp-content/uploads/2016/02/domesday-150x150.jpg",
                            "Tech",
                            "06")

ep_weather_other_planets = EpisodeInfo(
                            "Crazy Weather On Other Planets",
                            "http://www.cmpod.net/astronomy-shorts-3-crazy-weather-planets/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/gt3kzf/AS3_Weather_Other_plantes.mp3",
                            "http://www.cmpod.net/all-transcripts/astronomy-shorts-3-crazy-weather-planets-text/",
                            "A series of short episodes that will give you a taste of the very diverse field of astronomy. Each episode will reveal fascinating details and facts about celestial objects, space, and our universe as a whole.",
                            "http://www.cmpod.net/wp-content/uploads/2016/03/512px-Hoags_object-150x150.jpg",
                            "Science",
                            "07")

ep_molecular_clk_part1 = EpisodeInfo(
                            "The Molecular Clock Part I",
                            "http://www.cmpod.net/the-real-adam-and-eve-the-molecular-clock-part-i/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/jsrpew/CMPod_Molecular_Clock_Part1.mp3",
                            "http://www.cmpod.net/all-transcripts/the-real-adam-and-eve-the-molecular-clock-text/",
                            "The Molecular Clock technique was invented by Emile Zuckerkandl. Several decades later, Dr. Rebecca Cann, who examined samples of Mitochondrial DNA, made an amazing discovery: she confirmed the existence of a single  Mitochondrial Eve, and solved a Paleoanthropological mystery: Earth was once home to many different Human Species – from Homo Erectus to the Neanderthals. Yet today, they are all gone. When and how did the other humanoids disappear? The answer is hidden, of all places, in out DNA.",
                            "http://www.cmpod.net/wp-content/uploads/2015/11/640px-Huxley_-_Mans_Place_in_Nature-150x150.jpg",
                            "Science",
                            "08")

ep_rontgen_part1 = EpisodeInfo(
                            "Medical History: Rontgen, Hounsfield & Radiology",
                            "http://www.cmpod.net/the_story_of_x_rays/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/cirbj8/CM_EP_XRays.mp3",
                            "http://www.cmpod.net/all-transcripts/with-a-little-help-from-the-beatles-the-story-of-x-rays-ct-text/",
                            "In 1895, Wilhelm Röntgen made an accidental discovery that forever changed the medical profession: X-Rays. He was the first to solve the puzzle of a peculiar device named the “Crookes Tube”, and ushered in a new field of research: Radiology.",
                            "http://www.cmpod.net/wp-content/uploads/2015/09/rontgen-150x150.jpg",
                            "Science",
                            "09")

ep_arsenic_part1 = EpisodeInfo(
                            "Arsenic Poisoning – A History",
                            "http://www.cmpod.net/the-history-of-poisons/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/mndv92/CMPod_History_Of_Poisons_V1_1.mp3",
                            "http://www.cmpod.net/all-transcripts/the-poison-king-on-the-history-of-poisons-text/",
                            "Poisons are an integral part of human history, as the story of king Mithridates reveals. But when Life Insurance was invented, poisoning became a plague in Victorian Britain. For many women, Arsenic poisoning was the perfect murder weapon – as was the case with Lady Charlotte Elizabeth Ursinus. Discover why Arsenic was known as the ‘inheritance powder’, and the biological mechanism that makes it so deadly. ",
                            "http://www.cmpod.net/wp-content/uploads/2016/01/Poison_cr-150x134.jpg",
                            "Science",
                            "10")

ep_lsd_part1 = EpisodeInfo(
                            "The History of LSD, Part 1",
                            "http://www.cmpod.net/the-history-of-lsd-pt-1-how-does-it-feel-to-be-crazy/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/9y3nat/CMPod_History_Of_LSD_Pt1.mp3",
                            "http://www.cmpod.net/all-transcripts/the-history-of-lsd-text/",
                            "When Albert Hofmann accidentally discovered Lysergic Acid Diethylamide – LSD – he hoped that the unusual compound would help psychiatrists treat patients by inducing ‘temporary insanity’. It was the CIA who tested the LSD’s mind-bending potential as a psychological weapon, in a top-secret and horrifically cruel series of experiments known as MKULTRA.",
                            "http://www.cmpod.net/wp-content/uploads/2016/01/Timothy_Leary-150x150.jpg",
                            "Life",
                            "11")

ep_plague_part1 = EpisodeInfo(
                            "A Flea’s Worst Nightmare: The Black Death",
                            "http://www.cmpod.net/a-fleas-worst-nightmare-on-the-plague/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/jcmf75/EP_The_Plague_Final.mp3",
                            "http://www.cmpod.net/all-transcripts/a-fleas-worst-nightmare-on-the-plague-text/",
                            "In the 19th century, two brave (and some might say – insanely brave) French physicians took to the streets of Hong Kong and Bombay and risked their own lives in the name of ridding Mankind – and the fleas – from their worst nightmare: The Black Death. This is their story and the story of the humankind’s bitter enemy throughout the ages: the Bubonic Plague.",
                            "http://www.cmpod.net/wp-content/uploads/2015/12/565px-Danse_macabre_by_Michael_Wolgemut-e1449661494803-150x150.png",
                            "Life",
                            "12")

ep_sdi_part1 = EpisodeInfo(
                            "Ronald Reagan’s Strategic Defense (SDI) Initiative, AKA – “Star Wars”",
                            "http://www.cmpod.net/ronald-reagans-strategic-defense-initiative-aka-star-wars-curious-minds-podcast/",
                            "http://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/wbvzif/CM_SDI.mp3",
                            "http://www.cmpod.net/all-transcripts/ronald-reagans-strategic-defense-initiative-aka-star-wars-text/",
                            "In 1983, president Ronald Reagan shocked the world when he announced that the United States was developing an ultra-modern defense system against intercontinental ballistic missiles. Hundreds of billions of dollars were invested in the system’s development – But then, in 1991, the Soviet Union collapsed, and with it – the Star Wars initiative. Was Reagan’s Strategic Defense Initiative the reason for the Soviet Union’s collapse?",
                            "http://www.cmpod.net/wp-content/uploads/2016/12/640px-Space_Laser_Satellite_Defense_System_Concept-150x150.jpg",
                            "Tech",
                            "13")

ep_marine_nav_part1 = EpisodeInfo(
                            "Marine Navigation & The Scilly Islands Disaster",
                            "http://www.cmpod.net/marine-navigation-scilly-islands-disaster/",
                            "https://traffic.cast.plus/575ee6d40c1195111a89a08c/curiousminds.podbean.com/mf/play/ueki9u/CM_The_Longitude_Problem.mp3",
                            "http://www.cmpod.net/all-transcripts/marine-navigation-scilly-islands-disaster-text/",
                            "How a single navigation error cost the Royal Navy Four battleships and 1,505 men – and led a humble carpenter to solve one of the most difficult & important engineering challenges of the last 300 years.",
                            "http://www.cmpod.net/wp-content/uploads/2016/03/HMS_Association_1697-150x150.jpg",
                            "Humanities",
                            "14")

latest = ep_software_bugs_part1

recomended_episodes = [ep_software_bugs_part1, ep_file_sharing_part1, ep_indo_european_part1, ep_uboats_part1]
tech_episodes       = [ep_opensource_part1, ep_stuxnet_part1, ep_preservation_part1, ep_file_sharing_part1]
science_episodes    = [ep_weather_other_planets, ep_molecular_clk_part1, ep_rontgen_part1, ep_arsenic_part1]
life_episodes       = [ep_lsd_part1, ep_plague_part1, ep_molecular_clk_part1, ep_arsenic_part1]
humanities_episodes = [ep_sdi_part1, ep_marine_nav_part1, ep_lsd_part1, ep_indo_european_part1]

all_episodes = [ep_software_bugs_part1, ep_file_sharing_part1, ep_indo_european_part1,
                ep_uboats_part1, ep_opensource_part1, ep_stuxnet_part1, ep_preservation_part1,
                ep_weather_other_planets, ep_molecular_clk_part1, ep_rontgen_part1,
                ep_arsenic_part1, ep_lsd_part1, ep_plague_part1, ep_sdi_part1,
                ep_marine_nav_part1]

all_episodes_url = "http://www.cmpod.net/episodes/"
