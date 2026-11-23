---
title: Bernstein irreducibility and split places
decls:
  - GlobalTheory.CompanionTheory.BernBridge.Split.unrMaps_of_lt
  - GlobalTheory.CompanionTheory.BernBridge.Split.finSplit_of_narrow
  - GlobalTheory.CompanionTheory.BernNarrow.ramifiedMultiplicityOne_of_bernstein
  - GlobalTheory.CompanionTheory.BernNarrow.first_cohomology_ramified_narrow
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bernstein irreducibility and split places

This section proves that a narrow case of the irreducibility theorem of Bernstein gives two local inputs of the theta argument for the discrete series. The case is a product of two characters of determinants, each unitary. The first input is the existence of local theta data at the split places outside the bad set, which [Theorem 3.12.4](/entry/fin-split-of-geo/) uses. The second input is multiplicity one for local equivariant maps at the bad places, which [Theorem 3.12.6](/entry/ramified-multiplicity-one-of-geometric-filtration/) uses. The irreducibility enters in two ways. At good places, it makes two explicit zeta integrals onto an induced space. At bad places, it makes a space of Schwartz-Bruhat functions on full rank matrices irreducible modulo coinvariants. For background see [smooth representations of p-adic groups](/learn/representations/#smooth-representations-of-p-adic-groups) and [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module).

### Setting

Let $k$ be a nonarchimedean local field with ring of integers $\mathcal{O}$, residue field with $q$ elements and normalized absolute value $|\cdot|$. Put $G_n = \mathrm{GL}_n(k)$ and $K_n = \mathrm{GL}_n(\mathcal{O})$. A character $\chi : k^\times \to \mathbb{C}^\times$ is *smooth* if its kernel is open, *unitary* if $|\chi(x)| = 1$ for all $x$, and *unramified* if it is trivial on $\mathcal{O}^\times$. An unramified character is smooth. For a smooth character $\chi$ write $\chi_n = \chi \circ \det$, a one-dimensional representation of $G_n$. For smooth representations $\pi_1$ of $G_r$ and $\pi_2$ of $G_t$, let $\pi_1 \times \pi_2$ be the normalized parabolic induction $i_e(\pi_1 \otimes \pi_2)$ from the block upper triangular parabolic subgroup with blocks $r$ and $t$, as in Section 16. For a finite product $X$ of copies of $k$, let $\mathcal{S}(X)$ be the space of Schwartz-Bruhat functions on $X$, that is, the locally constant functions with compact support. We use Haar measures on $G_a$ that give $K_a$ volume $1$.

**Definition 1.19.1 (Narrow Bernstein property).** The *narrow Bernstein property* is the following statement. For every nonarchimedean local field $k$, all $a, b \in \mathbb{N}$ and all smooth unitary characters $\chi_1, \chi_2$ of $k^\times$ with $a \neq b$ or $\chi_1 \neq \chi_2$, the representation $\chi_{1,a} \times \chi_{2,b}$ of $G_{a+b}$ is irreducible.

**Theorem 1.19.2 (Bernstein).** Let $\pi_1$ and $\pi_2$ be irreducible smooth unitarizable representations of $G_r$ and $G_t$. Then $\pi_1 \times \pi_2$ is irreducible. Source: Bernstein, LNM 1041 (1984), consequence of the Kirillov conjecture proved there.

The narrow property is a special case. The results below assume only the narrow property.

### The induced space and the unramified maps

Fix $a, a' \in \mathbb{N}$ and put $d = a + a'$. Write elements of $G_d$ in blocks of sizes $a$ and $a'$, and call $b$ *block upper* if its lower left $a' \times a$ block is zero. Its diagonal blocks are then $A \in G_a$ and $D \in G_{a'}$.

**Definition 1.19.3 (Induced space).** For characters $\alpha, \beta$ of $k^\times$, let $I(\alpha, \beta)$ be the space of functions $F : G_d \to \mathbb{C}$ such that $F$ is right invariant under some open subgroup, and
$$F(bh) = \alpha(\det A)\,\beta(\det D)\,|\det A|^{a'/2}\,|\det D|^{-a/2}\,F(h)$$
for every block upper $b$ with diagonal blocks $A, D$ and every $h \in G_d$. The group $G_d$ acts on $I(\alpha, \beta)$ by right translation $R(h)F(x) = F(xh)$.

For smooth $\alpha, \beta$, the factor $|\det A|^{a'/2}|\det D|^{-a/2}$ is $\delta^{1/2}$ for the block parabolic subgroup, so $I(\alpha, \beta)$ is the space of $\alpha_a \times \beta_{a'}$, realized as functions.

**Lemma 1.19.4 (Irreducibility of the induced space).** Assume the narrow Bernstein property. Let $\alpha, \beta$ be smooth unitary characters and $a' < a$. Every subspace $N \subseteq I(\alpha, \beta)$ stable under right translation is $0$ or $I(\alpha, \beta)$.

Lean: `GlobalTheory.CompanionTheory.BernBridge.Split.indIrredLt_of`.

*Proof.* Since $a \neq a'$, the narrow property applies to $\alpha_a \times \beta_{a'}$. The pull back of $N$ to this induced representation is a subrepresentation, so it is $0$ or everything. $\square$

Now fix also $\varpi \in k^\times$ and a third character $\nu$. On $\mathcal{S}(M_{a \times d}(k))$ and $\mathcal{S}(M_{a' \times d}(k))$ define, for $g$ in $G_a$ or $G_{a'}$ and $h \in G_d$,
$$\omega_A(g, h)\Phi(X) = \nu(\det g)^{-1}\beta(\det h)\,|\det g|^{-d/2}|\det h|^{-a/2}\,\Phi(g^{-1}X\,{}^t h^{-1}),$$
$$\omega_B(g, h)\Psi(Y) = \nu(\det g)\,\alpha(\det h)\,|\det g|^{d/2}|\det h|^{a'/2}\,\Psi({}^t g\,Y h).$$
Let $X_0 = (1_a \mid 0) \in M_{a \times d}(k)$ and $Y_0 = (0 \mid 1_{a'}) \in M_{a' \times d}(k)$. For $\varphi$ on $M_a(k)$ and $n \in \mathbb{Z}^a$ with $n_1 \geq \dots \geq n_a$, put
$$s_n(\varphi) = \int_{K_a \varpi^n K_a} \varphi(g)\,\nu(\det g)\,|\det g|^{d/2}\,dg, \qquad c_m(\varphi) = \sum_{n_1 + \dots + n_a = m} s_n(\varphi).$$
Let $P_a(T) = \prod_{i=0}^{a-1}(1 - \nu(\varpi)q^{i - d/2}T) = \sum_j p_j T^j$, and put $Z^\natural(\varphi) = \sum_{m \in \mathbb{Z}} \sum_{j=0}^{a} p_j\,c_{m-j}(\varphi)$. A sum with infinite support is read as $0$.

**Definition 1.19.5 (Unramified maps).** For $\Phi \in \mathcal{S}(M_{a \times d}(k))$ and $\Psi \in \mathcal{S}(M_{a' \times d}(k))$, let
$$p(\Phi)(h) = Z^\natural\bigl(g \mapsto \omega_A(1, h)\Phi(gX_0)\bigr),$$
$$p'(\Psi)(h) = P_{a'}(1)\,\alpha(\det h)\,|\det h|^{a'/2}\int_{G_{a'}} \Psi(gY_0h)\,\nu(\det g)\,|\det g|^{d/2}\,dg,$$
where $P_{a'}(T) = \prod_{i=0}^{a'-1}(1 - \nu(\varpi)q^{i-d/2}T)$.

**Definition 1.19.6 (Standing conditions).** The data $(a, a', \varpi, \alpha, \beta, \nu)$ satisfy the *standing conditions* if $\varpi$ is a uniformizer, $\alpha$ and $\beta$ are unitary, $\nu = \alpha/\beta$, $a' < a$, $a + a'$ is even, and there is $e \in \mathbb{N}$ with $\alpha$ and $\beta$ trivial on the units $x$ with $|x - 1| \leq |\varpi^e|$.

**Theorem 1.19.7 (Inputs on the unramified maps).** Assume the standing conditions with $\nu$ unramified. In items 2 and 5, assume also that $\beta$ is unramified for the claims on $p$ and that $\alpha$ is unramified for the claims on $p'$. Item 4 holds for all $\Phi$ and $\Psi$, with no conditions. For all $\Phi, \Phi_1 \in \mathcal{S}(M_{a \times d})$, $\Psi, \Psi_1 \in \mathcal{S}(M_{a' \times d})$, $c \in \mathbb{C}$, $g$ and $h$:
1. $p(\Phi + c\Phi_1) = p(\Phi) + c\,p(\Phi_1)$ and $p'(\Psi + c\Psi_1) = p'(\Psi) + c\,p'(\Psi_1)$;
2. $p(\Phi) \in I(\alpha, \beta)$ and $p'(\Psi) \in I(\alpha, \beta)$;
3. $p(\omega_A(g, 1)\Phi) = p(\Phi)$ and $p'(\omega_B(g, 1)\Psi) = p'(\Psi)$;
4. $p(\omega_A(1, h)\Phi) = R(h)p(\Phi)$ and $p'(\omega_B(1, h)\Psi) = R(h)p'(\Psi)$;
5. $p(\mathbf{1}_{M_{a\times d}(\mathcal{O})})(h) = 1$ and $p'(\mathbf{1}_{M_{a'\times d}(\mathcal{O})})(h) = 1$ for $h \in K_d$.

Sources: Godement and Jacquet, LNM 260 (1972), Sections 3 and 6, for the zeta integrals; Mínguez, Ann. Sci. ÉNS (4) 41 (2008), Section 3, for theta maps of type II dual pairs into induced representations.

Lean: `PositivityTheory.ThK.SplitLoc.Unr.p_lin` (also `p'_lin`, `p_mem`, `p'_mem`, `p_inv`, `p'_inv`, `p_equiv`, `p'_equiv`, `p_unit`, `p'_unit`).

**Theorem 1.19.8 (Unramified maps).** Assume that the conclusion of the Lemma on irreducibility of the induced space holds. Let $(a, a', \varpi, \alpha, \beta, \nu)$ satisfy the standing conditions, with $\alpha$ and $\beta$ unramified. Then $p$ and $p'$ have the properties 1 to 5 above, and $p$ maps $\mathcal{S}(M_{a \times d}(k))$ onto $I(\alpha, \beta)$ and $p'$ maps $\mathcal{S}(M_{a' \times d}(k))$ onto $I(\alpha, \beta)$.

Lean: `GlobalTheory.CompanionTheory.BernBridge.Split.unrMaps_of_lt` (also `GlobalTheory.CompanionTheory.BernBridge.Split.onto_of_irredLt`).

*Proof.* Since $\nu = \alpha/\beta$, the character $\nu$ is unramified, so the inputs apply. They give items 1 to 5. We prove that $p$ is onto; the proof for $p'$ is the same. Let $N$ be the image of $p$. By item 1, $N$ is a subspace, and by item 2, $N \subseteq I(\alpha, \beta)$. The operator $\omega_A(1, h)$ maps $\mathcal{S}$ into $\mathcal{S}$, so item 4 shows that $N$ is stable under right translation. By item 5, $p(\mathbf{1}_{M_{a\times d}(\mathcal{O})})(1) = 1$, so $N \neq 0$. Since $\alpha$ and $\beta$ are unramified, they are smooth, and $a' < a$. By the assumed irreducibility, $N = I(\alpha, \beta)$. $\square$

### Local data at split places

We use the notation of the theta argument in the chapter on the discrete series. There $F$ is a number field, $E/F$ is a quadratic extension with involution $\sigma$, $B$ is the base datum, $G$ is a pair of hermitian and skew hermitian spaces of dimensions $a$ and $a'$ with Weil models, and $X$ is a character datum with a finite bad set $T$ and characters $\alpha$, $\beta$, $\nu = \alpha/\beta$. A *triple* $(G, X, \omega, \omega')$ consists of two Weil representations $\omega$, $\omega'$ of the unitary groups on adelic Schwartz-Bruhat spaces, with the conditions of that chapter. For a place $v$, let $\mathcal{S}_v$ and $\mathcal{S}'_v$ be the local Schwartz-Bruhat spaces of the two models at $v$.

**Definition 1.19.9 (Split local data).** Let $(G, X, \omega, \omega')$ be a triple and $v$ a finite place. *Local data at $v$* are a complex vector space $\Pi_v$ and linear maps $p_v : \mathcal{S}_v \to \Pi_v$ and $p'_v : \mathcal{S}'_v \to \Pi_v$ with these properties:
1. $p_v$ and $p'_v$ are onto;
2. $p_v$ vanishes on the span of the vectors $\omega_v(g, 1)\phi - \phi$ for $g$ in the local unitary group of the first space, and $p'_v$ vanishes on the analogous span for $\omega'_v$;
3. for $h$ in the local unitary group $U(W)_v$, if $p_v(\phi) = p'_v(\phi')$, then $p_v(\omega(1,h)\phi) = p'_v(\omega'(1,h)\phi')$;
4. $\Pi_v \neq 0$;
5. every subspace $N \subseteq \Pi_v$ with $p_v(\omega(1,h)\phi) \in N$ whenever $p_v(\phi) \in N$ and $h \in U(W)_v$ is $0$ or $\Pi_v$;
6. if $v \notin T$, then $p_v(\phi^\circ_v) = p'_v(\phi'^\circ_v) \neq 0$, where $\phi^\circ_v$ and $\phi'^\circ_v$ are the vacuum vectors;
7. if $v \in T$ and $v$ is a base place, the zeta condition of that chapter holds.

**Theorem 1.19.10 (Split local data).** Assume the narrow Bernstein property. Let $(G, X, \omega, \omega')$ be a triple and let $v \notin T$ be a finite place such that there is an $F$-embedding $E \to F_v$. Then local data at $v$ exist.

Lean: `GlobalTheory.CompanionTheory.BernBridge.Split.finSplit_of_narrow` (also `GlobalTheory.CompanionTheory.BernBridge.Split.finSplit_of_lt`).

*Proof.* Fix an embedding $\tau : E \to F_v$ and let $\alpha_v$, $\beta_v$, $\nu_v$ be the characters of $F_v^\times$ obtained from $\alpha$, $\beta$, $\nu$ through $\tau$. Since $v \notin T$, the facts on split characters give that $\alpha_v$ and $\beta_v$ are unitary and unramified, that $\nu_v = \alpha_v/\beta_v$, and that a conductor bound holds. The triple gives $a' < a$ and $a + a'$ even. So $(a, a', \varpi_v, \alpha_v, \beta_v, \nu_v)$ satisfy the standing conditions. By the Lemma, the Theorem on unramified maps applies, and gives $p$ and $p'$ onto $\Pi_v = I(\alpha_v, \beta_v)$.

The split place dictionary identifies $\mathcal{S}_v$ with $\mathcal{S}(M_{a \times d}(F_v))$ and $\mathcal{S}'_v$ with $\mathcal{S}(M_{a' \times d}(F_v))$. Under it, the local unitary groups act through $\omega_A$ and $\omega_B$, the map from $U(W)_v$ to $G_d$ is onto, and the vacuum vectors become $\mathbf{1}_{M(\mathcal{O})}$. Compose $p$ and $p'$ with these identifications. Item 3 of the inputs gives property 2. Item 4 gives property 3 and, with the Lemma, property 5. Since $p(\mathbf{1}_{M(\mathcal{O})})(1) = 1$, property 4 holds. For property 6, the function $p(\mathbf{1}_{M(\mathcal{O})}) - p'(\mathbf{1}_{M(\mathcal{O})})$ lies in $I(\alpha_v, \beta_v)$ and vanishes on $K_d$ by item 5. By the Iwasawa decomposition $G_d = PK_d$, an element of $I(\alpha_v, \beta_v)$ that vanishes on $K_d$ is $0$. Property 7 is empty, since $v \notin T$. $\square$

### Multiplicity one at bad places

Let $(G, X, \omega, \omega', R, R_f)$ and $(G_1, X, \omega_1, \omega'_1, R_1, R_{1,f})$ be two matched triples of the theta argument, with $G$ of sizes $(a, a')$ and $G_1$ of sizes $(a_1, a'_1)$. Here $R_f$ gives local data $(\Pi_v, p_v, p'_v)$ at all finite places. A *step* from $G$ to $G_1$ is one of two cases: $a_1 = a$, $a'_1 + 2 = a'$, $\chi = \beta$, $r = a/2$; or $a_1 + 2 = a$, $a'_1 = a'$, $\chi = \alpha$, $r = a'/2$. In each case one signature index of the matching space drops by one and the other stays fixed. Let $H'$ be a plane adapted to the step. A linear map $\lambda : \Pi_v \to \Pi_{1,v}$ is *equivariant* if, for every Levi element $(t, h_1, m)$ of $H'$, every unipotent $u$ of $H'$ in $U(W)_v$, and all $\phi, \phi_1$, the equality $\lambda(p_v\phi) = p_{1,v}\phi_1$ implies
$$\lambda\bigl(p_v(\omega(1, um)\phi)\bigr) = \chi(t)\,|t|_E^{\,r}\;p_{1,v}\bigl(\omega_1(1, h_1)\phi_1\bigr).$$

**Theorem 1.19.11 (Multiplicity one at bad places).** Assume the narrow Bernstein property. Let the two matched triples, the step and the adapted plane be as above, and let $v \in T$. Let $\lambda, \lambda' : \Pi_v \to \Pi_{1,v}$ be equivariant with $\lambda \neq 0$. Then $\lambda' = c\lambda$ for some $c \in \mathbb{C}$.

Lean: `GlobalTheory.CompanionTheory.BernNarrow.ramifiedMultiplicityOne_of_bernstein` (also `GlobalTheory.CompanionTheory.BernNarrow.first_cohomology_ramified_narrow`, `GlobalTheory.CompanionTheory.BernNarrow.pair_multiplicity_one_ramified`, `GlobalTheory.CompanionTheory.BernNarrow.local_multiplicity_one_irreducible_GL`).

*Proof.* Step 1: an action on the target. Fix the embedding $\tau$ of the base datum at $v$. Since $p_{1,v}$ is onto, every $x \in \Pi_{1,v}$ is $p_{1,v}(\phi)$. For $h \in U(W_1)_v$ put $\tau(h)x = p_{1,v}(\omega_1(1, h)\phi)$. Property 3 of the local data, applied to differences, shows that this does not depend on $\phi$. So $\tau(h)$ is a well defined linear map with $\tau(1) = 1$. By property 5, $\Pi_{1,v}$ is irreducible under $\tau$. It has countable dimension, since it is the image of a Schwartz-Bruhat space, and such a space has countable dimension.

Step 2: transfer. Let $\Lambda = \lambda \circ p_v$ in the first case of the step and $\Lambda = \lambda \circ p'_v$ in the second case, and define $\Lambda'$ in the same way. Property 2 of the local data shows that $\Lambda$ kills the coinvariants of the first unitary group. The equivariance of $\lambda$ and property 3 show that $\Lambda$ transforms under the parabolic subgroup of $H'$ by $\chi(t)|t|_E^r$ and $\tau(h_1)$. Since $v \in T$, the local character $\nu_v$ is ramified.

Step 3: the local theorem. At $v$ the dictionary identifies the Weil model with $\mathcal{S}(M_{n \times d}(F_v))$, and $U(W_1)_v$ maps onto $G_{d_1}(F_v)$. Consider the functions that vanish off the matrices of rank $n$, modulo the span of the vectors $\omega_B(g, 1)\Phi - \Phi$. This quotient is induced from a fibre representation of $G_n \times G_t$, with $d = n + t$. By the narrow Bernstein property for $1_n \times \mu_t$, with $\mu$ a ramified unitary character and hence $\mu \neq 1$, every stable subspace that contains the twisted coinvariants is everything or lies in them. With the irreducibility of $\tau$ and the countable dimension, a Schur argument then shows that two such maps into $\Pi_{1,v}$ that do not vanish on full rank functions are proportional on $\mathcal{S}$. This gives $c$ with $\Lambda' = c\Lambda$ on $\mathcal{S}_v$.

Step 4: conclusion. Since $p_v$ and $p'_v$ are onto, $\lambda' = c\lambda$. $\square$

The narrow property is used only with $a \neq b$, in the Lemma, and with $\chi_1 = 1 \neq \chi_2$, in Step 3. This is why the extra condition costs nothing.

**Remark 1.19.12 (Formalization).** The four results are in [FinSplitOfNarrow.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/FinSplitOfNarrow.lean#L187) and [LocalMultiplicityOneIrreducibleGL.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LocalMultiplicityOneIrreducibleGL.lean#L478). The narrow property is defined twice, as `NarrowBernstein` (FinSplitOfNarrow.lean L17) and as `Narrow` (LocalMultiplicityOneIrreducibleGL.lean L14), and `finSplit_of_narrow` and `first_cohomology_ramified_narrow` restate it in full instead of citing either. The name `first_cohomology_ramified_narrow` (L478) does not describe its content, which is the multiplicity one statement `RamifiedMultiplicityOne`; it is a one-line alias of `ramifiedMultiplicityOne_of_bernstein` (L390). A second proof of that statement, from the general hypothesis `GlobalTheory.Published.BernsteinUnitaryProductIrreducible`, is `ramifiedMultiplicityOne_of_bernstein` at L228 of [RamifiedMultiplicityOneOfBernstein.lean](lean:Development/WeilBound/ThetaLifts/LocalTheory/DixmierCommutants/RamifiedMultiplicityOneOfBernstein.lean#L228); the local steps `irr_gen`, `irr_ind`, `irrF'`, `local_multiplicity_one_irreducible_GL` and `pair_multiplicity_one_ramified` (L25, L93, L145, L190, L262) are copies with the narrow hypothesis. In the same way `finSplit_of_lt` (L121) parallels `finSplit_of` in SplitFin.lean, whose irreducibility hypothesis `IndIrred` has no smoothness condition. The inputs on $p$ and $p'$ are in a module named UpperProjectionInverseTransposeRightInverse.lean. The Iwasawa step is `induced_vanish_of_vanish_on_integral` and the dictionary is `split_place_dictionary`. We read the global definitions `IsTriple`, `IsMatched`, `IsZetaAt`, `IsLevi` and `unip` only at the level used here and did not unfold them.
