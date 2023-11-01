#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	unsigned int cnt = 1;
	listint_t *x, *y, *new_node;

	if (!head)
		return (NULL);
	x = *head;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!x || x->n >= number)
	{
		new_node->next = x, *head = new_node;
		return (new_node);
	}
	while (x->next && x->next->n < number)
		x = x->next;
	new_node->next = x->next, x->next = new_node;
	return (new_node);
}
