import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
	type: 'content',
	// Type-check frontmatter using a schema
	schema: z.object({
		title: z.string(),
		// Transform string to Date object
		date: z.coerce.date(),
		published: z.union([z.string(), z.boolean()]).optional(), // Handle "No" string or boolean
        updatedDate: z.coerce.date().optional(),
        heroImage: z.string().optional(),
	}),
});

const projects = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        shortDesc: z.string(),
        date: z.coerce.date(),
        tech: z.string(),
        codeLink: z.string().optional(),
        webHost: z.string().optional(),
        selfHost: z.string().optional(),
        dockerLink: z.string().optional(),
    }),
});

export const collections = { blog, projects };
