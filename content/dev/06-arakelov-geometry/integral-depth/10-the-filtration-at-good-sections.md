---
title: The filtration at good sections
decls:
  - GlobalTheory.HSShort.flatAt_of_simpleAt
  - GlobalTheory.T.hilbertSamuel_filtration_at_good_sections
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The filtration at good sections

The slope bound of the next section works with a system of vector spaces $V_0, V_1, \dots, V_T$ inside one space $A$ with a multiplication by linear forms. At a linear section $s$ it needs a filtration of the sections by their order of vanishing along the $D$ hyperplanes of $s$, with an explicit symbol on each graded piece, and it needs the Chow form to split at $s$. We call these data a *flat structure* at $s$. This section shows that the hermitian system of hermitian data has a flat structure at every section that is simple in the sense of [the Bertini theorem](/entry/bertini/). The result is used in [the explicit arithmetic Hilbert-Samuel bound](/entry/geo-bound-of-abstract/).

We use the hermitian data $X$ over a number field $F$, the geometric hypotheses and the quoted theorems $\mathsf{Q}$ of the previous sections. Write $D$ for the dimension of the image of $X$, $N$ for the number of its sections and $T$ for its length.

**Definition 3.10.1 (Hermitian system).** Let $F$ be a number field. A *hermitian system* $S$ over $F$ consists of:

1. natural numbers $N$, $n$, $D$, $T$, an $N \times n$ matrix $w$ over $F$ and, for each embedding $\sigma : F \to \mathbb{C}$, an $N \times N$ complex matrix $\mathrm{fr}_\sigma$;
2. an $F$-vector space $A$ with an $\mathcal{O}_F$-module structure compatible with the $F$-structure, and an $F$-linear map $u \mapsto \mu(u)$ from $F^N$ to the endomorphisms of $A$;
3. for each $j \in \mathbb{N}$ an $F$-subspace $V_j \subset A$, an $\mathcal{O}_F$-submodule $M_j \subset V_j$ and a family of hermitian norms $\|\cdot\|_{j,\sigma}$ on $V_j$, one for each $\sigma$;
4. real numbers $\beta$, $\Lambda$, $\Lambda_0$, $\Lambda_D$ and $\Lambda_T$.

For $u_1, \dots, u_t \in E^N$ we write $\mu(u_1, \dots, u_t) = \mu(u_1) \cdots \mu(u_t)$. For $s = (s_1, \dots, s_D)$ with $s_i \in E^N$ and a multi-index $\alpha \in \mathbb{N}^D$ we write $s^\alpha = \mu(s_1)^{\alpha_1} \cdots \mu(s_D)^{\alpha_D}$. For $a \in \mathbb{N}$ let $\mathrm{Mon}_a$ be the set of monomials of degree $a$ in $D$ variables, identified with the multi-indices $\alpha$ with $|\alpha| = a$.

The hermitian data $X$ give a hermitian system $S_X$ for each $\Lambda_0$: $A$ is the space of all sections of all weights, $\mu$ is the multiplication by the $N$ sections of the tuple, $V_j$ is the space of sections of weight $j$, $M_j$ and the norms are the lattices and norms of $X$, and the constants are those of $X$ together with $\Lambda_0$. We do not unfold this construction further.

**Definition 3.10.2 (Flat structure).** Let $S$ be a hermitian system over $F$, $E$ a field that contains $F$, $s \in E^{D \times N}$ and $\delta \in \mathbb{N}$. A *flat structure* of $S$ at $s$ of degree $\delta$ over $E$ consists of the following data.

1. An $E$-vector space $A'$ and a map $\iota : A \to A'$ that is additive and satisfies $\iota(c x) = c \iota(x)$ for $c \in F$. If $v_1, \dots, v_m \in V_T$ are linearly independent over $F$, then $\iota(v_1), \dots, \iota(v_m)$ are linearly independent over $E$.
2. An $E$-linear map $\mu'$ from $E^N$ to the endomorphisms of $A'$, with commuting values, such that $\mu'(u)\iota(x) = \iota(\mu(u) x)$ for $u \in F^N$ and $x \in A$. We write $s^\alpha$ and $\mu'(l_1, \dots, l_t)$ for the products of the values of $\mu'$ as above.
3. Points $y_1, \dots, y_\delta \in E^N$, all nonzero.
4. An $E$-linear map $\mathrm{res} : A' \to E^\delta$ that maps the $E$-span $V'_0$ of $\iota(V_0)$ onto $E^\delta$. Write $V'_D$ for the $E$-span of $\iota(V_D)$.
5. Subspaces $U_a \subset A'$ for $a \in \mathbb{N}$ and $E$-linear maps
$$\mathrm{sym}_a : U_a \to E^{\mathrm{Mon}_a \times \{1, \dots, \delta\}}.$$

For every $a < T - D$ these data satisfy:

- $U_{a+1} \subset U_a$, and $x \in U_a$ has $\mathrm{sym}_a(x) = 0$ if and only if $x \in U_{a+1}$;
- for every $\alpha \in \mathrm{Mon}_a$, all $l_1, \dots, l_{T-a} \in E^N$ and every $m \in V'_0$, the element $x = s^\alpha \mu'(l_1, \dots, l_{T-a}) m$ lies in $U_a$, and for $\alpha' \in \mathrm{Mon}_a$ and $1 \le p \le \delta$
$$\mathrm{sym}_a(x)(\alpha', p) = [\alpha' = \alpha] \prod_{q = 1}^{T - a} \langle l_q, y_p \rangle \, \mathrm{res}(m)_p,$$
where $\langle l, y \rangle = \sum_k l_k y_k$ and $[\alpha' = \alpha]$ is $1$ or $0$.

Finally, the deepest step is spanned by multiples of $V'_D$:
$$U_{T - D} = \sum_{\alpha \in \mathrm{Mon}_{T - D}} s^\alpha V'_D.$$

In the application $U_a$ is the space of sections that vanish to order at least $a$ along the linear section, $\mathrm{res}$ is the restriction to the $\delta$ points of the cut, and $\mathrm{sym}_a$ is the leading term of a section in the $D$ local equations $s_1, \dots, s_D$ at each point. The rule for monomials says that $s^\alpha$ has leading term the monomial $\alpha$, and that a product of linear forms $l_q$ acts on the leading term by its values at the point $y_p$.

**Definition 3.10.3 (Flat at a section).** Let $S$ be a hermitian system over $F$, $\delta \in \mathbb{N}$, $f$ a polynomial over $F$ in $D + 1$ groups of $N$ variables and $s \in F^{D \times N}$. Then $S$ is *flat at $s$* for $(\delta, f)$ if there are a field $E \supset F$, a flat structure of $S$ at $s$ of degree $\delta$ over $E$ with points $y_1, \dots, y_\delta$, and $c \in E$ with $c \ne 0$, such that
$$f(s) = c \prod_{p = 1}^{\delta} \ell_{y_p}.$$

Here $f(s)$ and $\ell_y$ are as in [the definition of a simple section](/entry/bertini/). So flatness at $s$ asks for the factorization of a simple section, now with points that are rational over $E$, together with the filtration.

**Theorem 3.10.4 (Filtration at good sections).** Assume the quoted theorems. Let $F$ be a number field, $X$ hermitian data over $F$ and $\Lambda_0 \in \mathbb{R}$ such that the geometric hypotheses hold for $X$ at $\Lambda_0$. Let $\delta \in \mathbb{N}$, let $f$ be a polynomial over $F$ in $D + 1$ groups of $N$ variables, and let $Q$ be a polynomial over $F$ in $D N$ variables. Assume that for every number field $E \supset F$ and every $s \in E^{D \times N}$ with $Q(s) \ne 0$, the section $s$ is simple for the tuple of $X$, $\delta$ and $f$. Then for every $s \in F^{D \times N}$ with $Q(s) \ne 0$, the system $S_X$ is flat at $s$ for $(\delta, f)$.

Lean: `GlobalTheory.HSShort.flatAt_of_simpleAt` (also `GlobalTheory.T.hilbertSamuel_filtration_at_good_sections`, a second name).

*Proof.* Let $s \in F^{D \times N}$ with $Q(s) \ne 0$. We build $E$, the flat structure and $c$.

*The splitting field.* Apply the assumption with $E = F$: the section $s$ is simple over $F$. In particular it is good. An input lemma on good sections gives a number field $E \supset F$ over which the cut splits: every geometric point of the cut is defined over $E$. The value $Q(s)$ stays nonzero in $E$, so the assumption, now over $E$, shows that $s$ is simple over $E$. Its base change to $E$ is a good section of the base change of $X$.

*The points and the constant.* An input lemma on specialized forms gives coordinates $y_1, \dots, y_\delta \in E^N$ of the $\delta$ points of the cut, all nonzero, and $c \in E$ with $c \ne 0$ and $f(s) = c \prod_p \ell_{y_p}$. This lemma takes the factorization of a simple section over $\bar E$ and uses that the points are rational over $E$.

*Base change of the hypotheses.* The line bundles $L$ and $L_2$ stay nef and big after the base change to $E$. The multiplication stays stable on the base change. For this last fact we use that $F$ is totally complex and that the multiplication is bounded by $\beta$, with $\beta > 0$; both are among the geometric hypotheses.

*The space and the maps.* Let $A'$ be the space of all sections of the base change of $X$ to $E$, let $\iota$ be the base change map and let $\mu'$ be the multiplication over $E$. An input lemma on base change shows that $\iota$ keeps linear independence on $V_T$, that $\mu'$ is compatible with $\iota$, and that the values of $\mu'$ commute.

*The filtration.* Let $U_a$ be the space of sections that vanish to order at least $a$ along the linear section, with its symbol map $\mathrm{sym}_a$, and let $\mathrm{res}$ be the residue map in degree $0$, that is, the restriction to the $\delta$ points. Five inputs give the conditions of a flat structure.

1. A lemma on the kernels of residues, which uses $\mathsf{Q}$, shows that the filtration decreases.
2. A lemma on residues in degree $0$, which uses $\mathsf{Q}$ and that $L_2$ is nef and big over $E$, shows that $\mathrm{res}$ maps $V'_0$ onto $E^\delta$.
3. A lemma on the total symbol shows that the kernel of $\mathrm{sym}_a$ is $U_{a+1}$.
4. A lemma on monomial products, which uses that the multiplication is stable over $E$, gives the formula for the symbol of $s^\alpha \mu'(l_1, \dots, l_{T-a}) m$.
5. A lemma on the deepest step, which uses item 1, that $L$ is nef and big over $E$ and that the multiplication is stable, shows that $U_{T - D}$ is the sum of the spaces $s^\alpha V'_D$.

Each of these lemmas is proved in the development; we do not reproduce them. The data assemble to a flat structure of $S_X$ at $s$ of degree $\delta$ over $E$, and with $c$ they show that $S_X$ is flat at $s$. $\square$

The main inputs are the vanishing theorems in $\mathsf{Q}$. They make the restriction to the points surjective in degree $0$ and show that a section that vanishes to order $T - D$ is a combination of the multiples $s^\alpha V'_D$. Without these two facts the symbols would not see all of $V'_0$ and the deepest part of the filtration could be larger than the image of $V_D$.

**Remark 3.10.5 (Formalization).** The quoted theorems enter only through the lemma on the kernels of residues and the lemma on residues in degree $0$ ([HilbertSamuelFiltrationAtGoodSections.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HilbertSamuelFiltrationAtGoodSections.lean#L27)). The hypothesis on simple sections is used only at $E = F$ and at the splitting field. The second name is a wrapper. We have not unfolded the space of all sections, the filtration by order of vanishing, the symbol or the splitting lemma; the description of $U_a$, $\mathrm{res}$ and $\mathrm{sym}_a$ above gives their role, not their definitions. The definition of a flat structure asks for the subspaces $U_a$ and the symbols for all $a$, but imposes conditions only for $a < T - D$ and at $a = T - D$ ([HermSysHypOneLeLambdaZero.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HermSysHypOneLeLambdaZero.lean#L196)).
