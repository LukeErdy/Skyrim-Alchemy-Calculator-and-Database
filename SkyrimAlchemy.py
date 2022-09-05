class Alchemy:

	def __init__(self):
		abacean_longfin = ['abacean longfin', 'weakness to frost', 'fortify sneak', 'weakness to poison', 'fortify restoration']
		ancestor_moth_wing = ['ancestor moth wing', 'damage stamina', 'fortify conjuration', 'damage magicka regen', 'fortify enchanting']
		ash_creep_cluster = ['ash creep cluster', 'damage stamina', 'invisibility', 'resist fire', 'fortify destruction']
		ash_hopper_jelly = ['ash hopper jelly', 'restore health', 'fortify light armor', 'resist shock', 'weakness to frost']
		ashen_grass_pod = ['ashen grass pod', 'resist fire', 'weakness to shock', 'fortify lockpicking', 'fortify sneak']
		bear_claws = ['bear claws', 'restore stamina', 'fortify health', 'fortify one-handed', 'damage magicka regen']
		bee = ['bee', 'restore stamina', 'ravage stamina', 'regenerate stamina', 'weakness to shock']
		beehive_husk = ['beehive husk', 'resist poison', 'fortify light armor', 'fortify sneak', 'fortify destruction']
		berits_ashes = ["berit's ashes", 'damage stamina', 'resist fire', 'fortify conjuration', 'ravage stamina']
		bleeding_crown = ['bleeding crown', 'weakness to fire', 'fortify block', 'weakness to poison', 'resist magic']
		blisterwort = ['blisterwort', 'damage stamina', 'frenzy', 'restore health', 'fortify smithing']
		blue_butterfly_wing = ['blue butterfly wing', 'damage stamina', 'fortify conjuration', 'damage magicka regen', 'fortify enchanting']
		blue_dartwing = ['blue dartwing', 'resist shock', 'fortify pickpocket', 'restore health', 'fear']
		blue_mountain_flower = ['blue mountain flower', 'restore health', 'fortify conjuration', 'fortify health', 'damage magicka regen']
		boar_tusk = ['boar tusk', 'fortify stamina', 'fortify health', 'fortify block', 'frenzy']
		bone_meal = ['bone meal', 'damage stamina', 'resist fire', 'fortify conjuration', 'ravage stamina']
		briar_heart = ['briar heart', 'restore magicka', 'fortify block', 'paralysis', 'fortify magicka']
		burnt_spriggan_wood = ['burnt spriggan wood', 'weakness to fire', 'fortify alteration', 'damage magicka regen', 'slow']
		butterfly_wing = ['butterfly wing', 'restore health', 'fortify barter', 'lingering damage stamina', 'damage magicka']
		canis_root = ['canis root', 'damage stamina', 'fortify one-handed', 'fortify marksman', 'paralysis']
		charred_skeever_hide = ['charred skeever hide', 'restore stamina', 'cure disease', 'resist poison', 'restore health']
		chaurus_eggs = ['chaurus eggs', 'weakness to poison', 'fortify stamina', 'damage magicka', 'invisibility']
		chaurus_hunter_antennae = ['chaurus hunter antennae', 'damage stamina', 'fortify conjuration', 'damage magicka regen', 'fortify enchanting']
		chickens_egg = ["chicken's egg", 'resist magic', 'damage magicka regen', 'waterbreathing', 'lingering damage stamina']
		creep_cluster = ['creep cluster', 'restore magicka', 'damage stamina regen', 'fortify carry weight', 'weakness to magic']
		crimson_nirnroot = ['crimson nirnroot', 'damage health', 'damage stamina', 'invisibility', 'resist magic']
		cyrodilic_spadetail = ['cyrodilic spadetail', 'damage stamina', 'fortify restoration', 'fear', 'ravage health']
		daedra_heart = ['daedra heart', 'restore health', 'damage stamina regen', 'damage magicka', 'fear']
		deathbell = ['deathbell', 'damage health', 'ravage stamina', 'slow', 'weakness to poison']
		dragons_tongue = ["dragon's tongue", 'resist fire', 'fortify barter', 'fortify illusion', 'fortify two-handed']
		dwarven_oil = ['dwarven oil', 'weakness to magic', 'fortify illusion', 'regenerate magicka', 'restore magicka']
		ectoplasm = ['ectoplasm', 'restore magicka', 'fortify destruction', 'fortify magicka', 'damage health']
		elves_ear = ['elves ear', 'restore magicka', 'fortify marksman', 'weakness to frost', 'resist fire']
		emperor_parasol_moss = ['emperor parasol moss', 'damage health', 'fortify magicka', 'regenerate health', 'fortify two-handed']
		eye_of_sabre_cat = ['eye of sabre cat', 'restore stamina', 'ravage health', 'damage magicka', 'restore health']
		falmer_ear = ['falmer ear', 'damage health', 'frenzy', 'resist poison', 'fortify lockpicking']
		felsaad_tern_feathers = ['felsaad tern feathers', 'restore health', 'fortify light armor', 'cure disease', 'resist magic']
		fire_salts = ['fire salts', 'weakness to frost', 'resist fire', 'restore magicka', 'regenerate magicka']
		fly_amanita = ['fly amanita', 'resist fire', 'fortify two-handed', 'frenzy', 'regenerate stamina']
		frost_mirriam = ['frost mirriam', 'resist frost', 'fortify sneak', 'ravage magicka', 'damage stamina regen']
		frost_salts = ['frost salts', 'weakness to fire', 'resist frost', 'restore magicka', 'fortify conjuration']
		garlic = ['garlic', 'resist poison', 'fortify stamina', 'regenerate magicka', 'regenerate health']
		giant_lichen = ['giant lichen', 'weakness to shock', 'ravage health', 'weakness to poison', 'restore magicka']
		giants_toe = ["giant's toe", 'damage stamina', 'fortify health', 'fortify carry weight', 'damage stamina regen']
		gleamblossom = ['gleamblossom', 'resist magic', 'fear', 'regenerate health', 'paralysis']
		glow_dust = ['glow dust', 'damage magicka', 'damage magicka regen', 'fortify destruction', 'resist shock']
		glowing_mushroom = ['glowing mushroom', 'resist shock', 'fortify destruction', 'fortify smithing', 'fortify health']
		grass_pod = ['grass pod', 'resist poison', 'ravage magicka', 'fortify alteration', 'restore magicka']
		hagraven_claw = ['hagraven claw', 'resist magic', 'lingering damage magicka', 'fortify enchanting', 'fortify barter']
		hagraven_feathers = ['hagraven feathers', 'damage magicka', 'fortify conjuration', 'frenzy', 'weakness to shock']
		hanging_moss = ['hanging moss', 'damage magicka', 'fortify health', 'damage magicka regen', 'fortify one-handed']
		hawk_beak = ['hawk beak', 'restore stamina', 'resist frost', 'fortify carry weight', 'resist shock']
		hawk_feathers = ['hawk feathers', 'cure disease', 'fortify light armor', 'fortify one-handed', 'fortify sneak']
		hawks_egg = ["hawk's egg", 'resist magic', 'damage magicka regen', 'waterbreathing', 'lingering damage stamina']
		histcarp = ['histcarp', 'restore stamina', 'fortify magicka', 'damage stamina regen', 'waterbreathing']
		honeycomb = ['honeycomb', 'restore stamina', 'fortify block', 'fortify light armor', 'ravage stamina']
		human_flesh = ['human flesh', 'damage health', 'paralysis', 'restore magicka', 'fortify sneak']
		human_heart = ['human heart', 'damage health', 'damage magicka', 'damage magicka regen', 'frenzy']
		ice_wraith_teeth = ['ice wraith teeth', 'weakness to frost', 'fortify heavy armor', 'invisibility', 'weakness to fire']
		imp_stool = ['imp stool', 'damage health', 'lingering damage health', 'paralysis', 'restore health']
		jarrin_root = ['jarrin root', 'damage health', 'damage magicka', 'damage stamina', 'damage magicka regen']
		jazbay_grapes = ['jazbay grapes', 'weakness to magic', 'fortify magicka', 'regenerate magicka', 'ravage health']
		juniper_berries = ['juniper berries', 'weakness to fire', 'fortify marksman', 'regenerate health', 'damage stamina regen']
		large_antlers = ['large antlers', 'restore stamina', 'fortify stamina', 'slow', 'damage stamina regen']
		lavender = ['lavender', 'resist magic', 'fortify stamina', 'ravage magicka', 'fortify conjuration']
		luna_moth_wing = ['luna moth wing', 'damage magicka', 'fortify light armor', 'regenerate health', 'invisibility']
		moon_sugar = ['moon sugar', 'weakness to fire', 'resist frost', 'restore magicka', 'regenerate magicka']
		mora_tapinella = ['mora tapinella', 'restore magicka', 'lingering damage health', 'regenerate stamina', 'fortify illusion']
		mudcrab_chitin = ['mudcrab chitin', 'restore stamina', 'cure disease', 'resist poison', 'resist fire']
		namiras_rot = ["namira's rot", 'damage magicka', 'fortify lockpicking', 'fear', 'regenerate health']
		netch_jelly = ['netch jelly', 'paralysis', 'fortify carry weight', 'restore stamina', 'fear']
		nightshade = ['nightshade', 'damage health', 'damage magicka regen', 'lingering damage stamina', 'fortify destruction']
		nirnroot = ['nirnroot', 'damage health', 'damage stamina', 'invisibility', 'resist magic']
		nordic_barnacle = ['nordic barnacle', 'damage magicka', 'waterbreathing', 'regenerate health', 'fortify pickpocket']
		orange_dartwing = ['orange dartwing', 'restore stamina', 'ravage magicka', 'fortify pickpocket', 'lingering damage health']
		pearl = ['pearl', 'restore stamina', 'fortify block', 'restore magicka', 'resist shock']
		pine_thrush_egg = ['pine thrush egg', 'restore stamina', 'fortify lockpicking', 'weakness to poison', 'resist shock']
		poison_bloom = ['poison bloom', 'damage health', 'slow', 'fortify carry weight', 'fear']
		powdered_mammoth_tusk = ['powdered mammoth tusk', 'restore stamina', 'fortify sneak', 'weakness to fire', 'fear']
		purple_mountain_flower = ['purple mountain flower', 'restore stamina', 'fortify sneak', 'lingering damage magicka', 'resist frost']
		red_mountain_flower = ['red mountain flower', 'restore magicka', 'ravage magicka', 'fortify magicka', 'damage health']
		river_betty = ['river betty', 'damage health', 'fortify alteration', 'slow', 'fortify carry weight']
		rock_warbler_egg = ['rock warbler egg', 'restore health', 'fortify one-handed', 'damage stamina', 'weakness to magic']
		sabre_cat_tooth = ['sabre cat tooth', 'restore stamina', 'fortify heavy armor', 'fortify smithing', 'weakness to poison']
		salmon_roe = ['salmon roe', 'restore stamina', 'waterbreathing', 'fortify magicka', 'regenerate magicka']
		salt_pile = ['salt pile', 'weakness to magic', 'fortify restoration', 'slow', 'regenerate magicka']
		scaly_pholiota = ['scaly pholiota', 'weakness to magic', 'fortify illusion', 'regenerate stamina', 'fortify carry weight']
		scathecraw = ['scathecraw', 'ravage health', 'ravage stamina', 'ravage magicka', 'lingering damage health']
		silverside_perch = ['silverside perch', 'restore stamina', 'damage stamina regen', 'ravage health', 'resist frost']
		skeever_tail = ['skeever tail', 'damage stamina regen', 'ravage health', 'damage health', 'fortify light armor']
		slaughterfish_egg = ['slaughterfish eggs', 'resist poison', 'fortify pickpocket', 'lingering damage health', 'fortify stamina']
		slaughterfish_scales = ['slaughterfish scales', 'resist frost', 'lingering damage health', 'fortify heavy armor', 'fortify block']
		small_antlers = ['small antlers', 'weakness to poison', 'fortify restoration', 'lingering damage stamina', 'damage health']
		small_pearl = ['small pearl', 'restore stamina', 'fortify one-handed', 'fortify restoration', 'resist frost']
		snowberries = ['snowberries', 'resist fire', 'fortify enchanting', 'resist frost', 'resist shock']
		spawn_ash = ['spawn ash', 'ravage stamina', 'resist fire', 'fortify enchanting', 'ravage magicka']
		spider_egg = ['spider egg', 'damage stamina', 'damage magicka regen', 'fortify lockpicking', 'fortify marksman']
		spriggan_sap = ['spriggan sap', 'damage magicka regen', 'fortify enchanting', 'fortify smithing', 'fortify alteration']
		swamp_fungal_pod = ['swamp fungal pod', 'resist shock', 'lingering damage magicka', 'paralysis', 'restore health']
		taproot = ['taproot', 'weakness to magic', 'fortify illusion', 'regenerate magicka', 'restore magicka']
		thistle_branch = ['thistle branch', 'resist frost', 'ravage stamina', 'resist poison', 'fortify heavy armor']
		torchbug_thorax = ['torchbug thorax', 'restore stamina', 'lingering damage magicka', 'weakness to magic', 'fortify stamina']
		trama_root = ['trama root', 'weakness to shock', 'fortify carry weight', 'damage magicka', 'slow']
		troll_fat = ['troll fat', 'resist poison', 'fortify two-handed', 'frenzy', 'damage health']
		tundra_cotton = ['tundra cotton', 'resist magic', 'fortify magicka', 'fortify block', 'fortify barter']
		vampire_dust = ['vampire dust', 'invisibility', 'restore magicka', 'regenerate health', 'cure disease']
		void_salts = ['void salts', 'weakness to shock', 'resist magic', 'damage health', 'fortify magicka']
		wheat = ['wheat', 'restore health', 'fortify health', 'damage stamina regen', 'lingering damage magicka']
		white_cap = ['white cap', 'weakness to frost', 'fortify heavy armor', 'restore magicka', 'ravage magicka']
		wisp_wrappings = ['wisp wrappings', 'restore stamina', 'fortify destruction', 'fortify carry weight', 'resist magic']
		yellow_mountain_flower = ['yellow mountain flower', 'resist poison', 'fortify restoration', 'fortify health', 'damage stamina regen']

		self.ingredient_array = [abacean_longfin, ancestor_moth_wing, ash_creep_cluster, ash_hopper_jelly, ashen_grass_pod, bear_claws, bee, beehive_husk, berits_ashes, bleeding_crown, blisterwort, blue_butterfly_wing, blue_dartwing, blue_mountain_flower, boar_tusk, bone_meal, briar_heart, burnt_spriggan_wood, butterfly_wing, canis_root, charred_skeever_hide, chaurus_eggs, chaurus_hunter_antennae, chickens_egg, creep_cluster, crimson_nirnroot, cyrodilic_spadetail, daedra_heart, deathbell, dragons_tongue, dwarven_oil, ectoplasm, elves_ear, emperor_parasol_moss, eye_of_sabre_cat, falmer_ear, felsaad_tern_feathers, fire_salts, fly_amanita, frost_mirriam, frost_salts, garlic, giant_lichen, giants_toe, gleamblossom, glow_dust, glowing_mushroom, grass_pod, hagraven_claw, hagraven_feathers, hanging_moss, hawk_beak, hawk_feathers, hawks_egg, histcarp, honeycomb, human_flesh, human_heart, ice_wraith_teeth, imp_stool, jarrin_root, jazbay_grapes, juniper_berries, large_antlers, lavender, luna_moth_wing, moon_sugar, mora_tapinella, mudcrab_chitin, namiras_rot, netch_jelly, nightshade, nirnroot, nordic_barnacle, orange_dartwing, pearl, pine_thrush_egg, poison_bloom, powdered_mammoth_tusk, purple_mountain_flower, red_mountain_flower, river_betty, rock_warbler_egg, sabre_cat_tooth, salmon_roe, salt_pile, scaly_pholiota, scathecraw, silverside_perch, skeever_tail, slaughterfish_egg, slaughterfish_scales, small_antlers, small_pearl, snowberries, spawn_ash, spider_egg, spriggan_sap, swamp_fungal_pod, taproot, thistle_branch, torchbug_thorax, trama_root, troll_fat, tundra_cotton, vampire_dust, void_salts, wheat, white_cap, wisp_wrappings, yellow_mountain_flower]

		self.choose()
	

	def choose(self):
		entry = input('What would you like to do?\n1. Learn about an ingredient\n2. Find ingredients by entering effects\n3. Find out what you can make from a list of ingredients\n\nEnter a number, 1-3: ')
		if entry == '1':
			self.search_ingredient()
		elif entry == '2':
			self.search_effects()
		elif entry == '3':
			self.find_potions()
		else:
			print('')
			self.choose()


	def search_ingredient(self):
		entry = input('\nEnter an ingredient: ')
		for ingredient in self.ingredient_array:
			if ingredient[0] == entry.lower():
				print('\nEffects of ' + entry.lower() + ': ' + ingredient[1] + ', ' + ingredient[2] + ', ' + ingredient[3] + ', ' + ingredient[4])
				print('\nYou can combine ' + entry.lower() + ' with:\n')
				entry = ingredient
				break
		for ingredient in self.ingredient_array:
			if ingredient[0] != entry[0] and list(set(ingredient) & set(entry)) != []:
				print(ingredient[0] + ' ' + str(list(set(ingredient) & set(entry))))
		print('')
		self.choose()


	def search_effects(self):
		entry = input('\nEnter an effect or a list of effects (use commas to separate effects, for example: fortify destruction, regenerate magicka): ')
		entry = entry.lower().split(', ')
		print('\nThe following ingredients possess the effect(s) ' + str(entry) + '\n')
		for ingredient in self.ingredient_array:
			if set(ingredient) & set(entry) == set(entry):
				print(ingredient[0])
		print('')
		self.choose()


	def find_potions(self):
		entry = input('\nEnter what you have to see what you can make (use commas to separate ingredients, for example: lavender, salt pile): ')
		entry = entry.lower().split(', ')
		ingredients = []
		print('\nWith ' + str(entry) + ', you can make:\n')
		for ingredient in self.ingredient_array:
			if ingredient[0] in entry:
				ingredients.append(ingredient)
		comparison_list = []
		for ingredient_0 in ingredients:
			for ingredient_1 in ingredients:
				if {ingredient_1[0], ingredient_0[0]} not in comparison_list and ingredient_1 != ingredient_0 and list(set(ingredient_1) & set(ingredient_0)) != []:
					print(str(list(set(ingredient_1) & set(ingredient_0))) + ' ' + ingredient_1[0] + ', '+ ingredient_0[0])
					comparison_list.append({ingredient_1[0], ingredient_0[0]})
		print('')
		self.choose()




def main():
	start = Alchemy()

if __name__ == '__main__':
	main()