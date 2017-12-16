from lightfm import LightFM
from lightfm.datasets import fetch_movielens
import numpy

data = fetch_movielens(min_rating=4.5)

model = LightFM(loss='warp')
model.fit(data['train'], epochs=10, num_threads=2)

def recommend(data, model, user_ids):
	num_ids, num_movies = data['train'].shape

	for user_id in user_ids:
		known_values = data['item_labels'][data['train'].tocsr()[user_id].indices]
		scores = model.predict(user_id, numpy.arange(num_movies))
		predicted_values = data['item_labels'][numpy.argsort(-scores)]

		print('		Known:')
		for movie in known_values[:3]:
			print('	%s' %movie)

		print('		Recommended:')
		for move in predicted_values[:3]:
			print('	%s' %move)
		print('\n')

recommend(data, model, [16,25,36])