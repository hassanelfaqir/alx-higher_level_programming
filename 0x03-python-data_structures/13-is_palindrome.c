#include "lists.h"

/**
 * is_palindrome - recursive palindrome or not palindrome.
 * @head : head list
 * return : 0 if not palindrome and 1 if is palindrome.
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (is_palind(head, *head));
}

/**
 * is_palind : function to know if is palind or not palind
 *
 * @head : head list
 *
 * @end : end
 * return : 1 if it is_palind 0 if not palind
 */

int is_palind(listint_t **head, listint_ *end)
{
	if (end == NULL)
		return (1);

	if (is_palind(head, end->next) && (*head)->n  == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
