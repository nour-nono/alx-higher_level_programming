#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * Return: True or False
 */
int is_palindrome(listint_t **head)
{
	listint_t **head_copy = head;

	if (head == NULL || *head == NULL)
		return (1);
	return (recursive_palindrom(head_copy, *head));
}
/**
 * recursive_palindrom - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @end: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
int recursive_palindrom(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (recursive_palindrom(head, end->next) && ((*head)->n == end->n))
	{
		(*head) = (*head)->next;
		return (1);
	}
	return (0);
}
