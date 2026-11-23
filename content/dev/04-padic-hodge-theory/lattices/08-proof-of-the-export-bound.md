---
title: Proof of the export bound
decls:
  - Formalism.MainNotions.TwistedPlaces.point_bound
  - Formalism.MainNotions.TwistedPlaces.export_bound_of_admissible
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Proof of the export bound

This section proves [the export bound for one datum](/entry/export-bound-of-admissible/), which the previous section stated and used for families. The proof has two steps. The first step groups the twisted places of a size datum by their residue characteristic $l$, so that the twisted sum is bounded by a global term plus a sum over primes $l$ of $\log l$ times a local length $\lambda_G(l)$. The second step, the point bound below, splits the primes into five classes and bounds the sum over each class by the conditions of the admitted inputs. The section keeps the notation of the previous section: the scale $(x, \varepsilon)$, the sizes $\mathcal{L}$ and $b$, the global datum $D$ with its integers $f, m, t$, and the size datum $\mathcal{S}$.

**Definition 8.8.1 (Local length at a prime).** Let $\mathcal{S}$ be a size datum for $D$, let $C \in \mathbb{R}$, and let a table of local lengths for $\mathcal{S}$ be given. The table gives a finite set $\mathrm{exc}$ of *exceptional* primes. The datum $D$ gives a finite set $\mathrm{small}$ of small primes that contains $2$, two primes $q$ and $d$, and a set $G_D$ of at most two primes. The size datum gives a positive number $\eta_{\mathrm{sz}}$ and the threshold
$$l^* = \frac{m\, b}{n t^2 (N_m + t)\, \mathcal{L}^2 + k n^2 (S_c + t + \mathcal{L})},$$
where $n, k, N_m$ are integers of $D$ and $S_c$ is a number of $\mathcal{S}$. For a prime $l$ put
$$\lambda_B(l) = \begin{cases} C f m\, b \log x + C x^C \mathcal{L}^2 & \text{if } l \in \mathrm{small} \text{ or } l = 3, \\ 2 C f m\, b & \text{else, if } l = q \text{ or } l = d, \\ 0 & \text{else, if } l > l^* \text{ and } l \notin \mathrm{exc}, \\ B + B'(l) & \text{otherwise}. \end{cases}$$
Here $B = C f n t^2 n_V \mathcal{L}^2$, with $n_V$ an integer of $D$, and $B'(l) \ge 0$ is a length bound at $l$ that depends on how $l$ splits in the fields of $D$. The *local length* at $l$ is $\lambda_G(l) = C x^C \eta_{\mathrm{sz}}$ if $l \in G_D$, and $\lambda_G(l) = \lambda_B(l)$ otherwise.

So a prime $l$ above the threshold $l^*$ costs nothing unless it is exceptional, and the cost of each other prime is a power of $x$ times $b$ or $\mathcal{L}^2$. The term $B'(l)$ is where the local bounds of the earlier sections enter: it is built from the lifting exponents and the row bounds at $l$.

We use one more size. For $C \in \mathbb{R}$ put
$$U = x^{C+2} \exp\bigl(x^{\varepsilon/4}\bigr).$$
Since $x^{C+2} e^{x^{\varepsilon/3}} \le e^{x^{\varepsilon}}$ on a large scale, every fixed power of $U$ is small against $b = e^{x^{\varepsilon}}$. The first step of the proof below makes this exact.

**Proposition 8.8.2 (Point bound).** Let $\mathcal{S}$ be a size datum for $D$ with parameters $P$, let $C > 0$, and assume that the parameters are polynomially bounded with constant $C$ and that the scale of $\mathcal{S}$ is large for $C$. Let a table of local lengths satisfy the seventeen conditions of the admitted inputs with constant $C$, and let $S$ be a finite set of primes. Then
$$\begin{aligned} 6 + \nu + \log h_E + \log |G| &+ \sum_{l \in S} \log l \cdot \lambda_G(l) \\ &\le 2000\, (C+1)^3\, f m\, b\, \mathcal{L}^2. \end{aligned}$$
Here $\nu$ is a number of $D$, $h_E$ is the positive integer of $D$ and $|G|$ the order of the finite group of $D$ that enter the polynomial bounds.

Lean: `Formalism.MainNotions.TwistedPlaces.point_bound`.

*Proof.* Put $X = f m\, b\, \mathcal{L}^2$. Since $m \ge 1$, $f \ge m$, $\mathcal{L} \ge 1$ and $b \ge 1$, we have $b \le X$.

First we compare $U$ with $b$. From the conditions of a large scale and $C > 0$ one gets $4 \cdot 10^6 (C+1)^2 U^{18} \le b$: the factor $4 \cdot 10^6 (C+1)^2$ is at most $x^2$ since $10^8 (C+1)^3 \le x$, and $x^{20C + 40} e^{20 x^{\varepsilon/4}} \le e^{x^{\varepsilon/3}} \le e^{x^{\varepsilon}}$ absorbs the rest.

Second, the global term. The polynomial bounds give $\log h_E \le C x^C$ and $\log |G| \le C x^C \mathcal{L}$, and bounds on the ranks of $D$ give $\nu \le 12 (C+1)^2 U^{18}$. Together,
$$6 + \nu + \log h_E + \log |G| \le 20 (C+1)^2 U^{18}.$$

Third, we bound each summand $\log l \cdot \lambda_G(l)$ by the sum of five terms, one for each class of primes: the term for $G_D$ if $l \in G_D$; the term for small primes if $l \in \mathrm{small}$ or $l = 3$; the term for $q, d$ if $l = q$ or $l = d$; the term $\log l \cdot (B + B'(l))$ if $l \ne 2, 3$ and $l \le l^*$; and the same term if $l \in \mathrm{exc}$ and $l > l^*$. Each of the five terms is $0$ outside its class and is nonnegative. We check the bound by the case split in the definition of $\lambda_G$. The only case that needs a remark is the last one of $\lambda_B$: then $l \notin \mathrm{small}$, so $l \ne 2$, and $l \ne 3$; if $l \le l^*$ the fourth term is present, and if $l > l^*$ then $l \in \mathrm{exc}$, so the fifth term is present. Summing over $S$ and sorting the terms, the sum over $S$ is at most the sum of five sums, each over the primes of $S$ in one class.

Fourth, the five sums. With the polynomial bounds and the large scale:

- the sum over $G_D$ is at most $2 (C+1)^2 U^{18}$, since $G_D$ has at most two primes and $\log l$, $x^C$ and $\eta_{\mathrm{sz}}$ are bounded by powers of $U$;
- the sum over the small primes and $3$ is at most $8 C X$;
- the sum over $q$ and $d$ is at most $4 C X$, since $\log q$ and $\log d$ are at most $\mathcal{L}$;
- the sum over the primes $l \le l^*$ with $l \ne 2, 3$ is at most $1000 (C+1)^3 X$; here every such $l$ is at least $5$, the sum of the terms $\log l \cdot B$ is bounded with the threshold $l^*$, and each part of $B'(l)$ is bounded by a sum over the primes $l \le l^*$;
- the sum over the exceptional primes $l > l^*$ is at most $1164000 (C+1)^2 U^{18}$. This uses two of the seventeen conditions: at a large prime that is not exceptional the local lengths vanish, and the exceptional primes are bounded.

Last, we add. The three terms in $U^{18}$ and the global term give
$$(20 + 2 + 1164000)(C+1)^2 U^{18} \le 4 \cdot 10^6 (C+1)^2 U^{18} \le b \le X.$$
So the left side is at most $1000 (C+1)^3 X + 8 C X + 4 C X + X$. Since $(C+1)^3 = C^3 + 3C^2 + 3C + 1$ and $C > 0$, we have $1000 (C+1)^3 + 12 C + 1 \le 2000 (C+1)^3$, and the bound follows. $\square$

The grouping step is the following inequality. Let the admitted inputs hold with a table of local lengths, and let $\sum_l v(l)$ converge, with $v(l)$ the Tate-Shafarevich term of the previous section. Then for every lift $j$,
$$\begin{aligned} \Sigma_j(\mathcal{S}) \le d_0(j) \Bigl( 6 + \nu &+ \log h_E + \log |G| + \sum_{l \in S} \log l \cdot \lambda_G(l) \Bigr) \\ &+ d_0(j) \sum_l v(l), \end{aligned}$$
where $S$ is the set of residue characteristics of the twisted places in $\mathrm{supp}$. Each twisted place $w$ above $l$ contributes $\lambda(w) e(w) \eta_j(w)$, and the conditions of the admitted inputs bound the sum of these contributions over the places above $l$ by $d_0(j) \log l \cdot \lambda_G(l)$, up to the global and Tate-Shafarevich terms.

*Proof of [the export bound for one datum](/entry/export-bound-of-admissible/).* Let the scale be large for $C$ and let the admitted inputs with constant $C$ hold for $(\mathcal{S}, P)$. Assume that each $\ell'_p(e)$ is finite and that $\sum_l v(l)$ converges, and let $j$ be a lift. The admitted inputs give a table of local lengths that satisfies the seventeen conditions. The last condition bounds a constant of $P$ by $C$, and this constant is positive, so $C > 0$ and $|C| = C$. The last condition also says that the parameters are polynomially bounded with constant $C$. The grouping step gives the inequality above, with $S$ the set of residue characteristics of the twisted places in $\mathrm{supp}$; each element of $S$ is a prime. The point bound for this $S$ bounds the bracket by $2000 (C+1)^3 X$, with $X = f m\, b\, \mathcal{L}^2$. The number $N_c$ is a quotient of nonnegative numbers, so $N_c \ge 0$ and $X \le X + (\log x)^2 N_c$. Since $d_0(j) \ge 0$, we get
$$\Sigma_j(\mathcal{S}) \le d_0(j) \Bigl( 2000 (C+1)^3 \bigl( X + (\log x)^2 N_c \bigr) + \sum_l v(l) \Bigr),$$
which is the export bound with constant $2000 (|C| + 1)^3$. $\square$

**Remark 8.8.3 (Formalization).** The grouping step is `etaSum_le` (MemPrimesOverOfMem.lean line 558); it is not in the decls of this chapter, and we did not open its proof. It has a hypothesis `_hg2` that no prime of $G_D$ is $2$, and the sign `_` at the start of its name marks it as unused; the proof of the export bound still supplies it, as `gset_ne_two` ([ExportBoundOfAdmissible.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ExportBoundOfAdmissible.lean#L1008)). The local length is `lamG` and $\lambda_B$ is `lamB` (MemPrimesOverOfMem.lean lines 259 and 528); $B$ is `bbB`, $B'(l)$ is `lenB` (line 249), and we did not unfold the quantities inside `lenB`. The five sums are `sum_g`, `sum_23`, `sum_qd`, `sum_small` and `sum_exc`, the global term is `glob_le`, and the comparison of $U$ with $b$ is `big_le_b` (ExportBoundOfAdmissible.lean lines 18 to 825). The two conditions used in `sum_exc` are the twelfth and thirteenth of `AdmT`, named `LargePrimeLengthVanishing` and `ExceptionalPrimesBounded`; other declarations elsewhere in the library carry the name `LargePrimeLengthVanishing` with a different meaning.
