---
title: Hecke operators and the second branch
decls:
  - Formalism.L2.GlobalTheoryTheory.UnramifiedTrace.hecke_ramified_zero_all
  - Formalism.L2.GlobalTheoryTheory.LemB.second_branch_all_members
  - Formalism.L2.GlobalTheoryTheory.LemB.second_branch_of_rationality
  - Formalism.L2.GlobalTheoryTheory.LemB.second_branch_of_surjectivity
  - Formalism.L2.GlobalTheoryTheory.LemB.second_branch_of_coordinates_and_count
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hecke operators and the second branch

The mass formula counts the classes of a genus. The [local matching of theta lifts](/step/theta-local-matching/) needs two more facts about the space of functions on these classes at level zero, for the members of a family of global data in the Hida setting. The first is an identity of Hecke operators at a ramified place: the up operator $U_v$ and the down operator $D_v$ preserve the ramified part, and $U_v D_v$ acts on it as a power of the uniformizer $T$. The second is the *second branch*: a length formula for the quotient of two lattices of the level-zero space at a place over $T$. The length is the product of the ramification index, the number of level-zero classes times the rank of a Weyl module, and the weight. We keep the notation of the [slope of the ramified line](/entry/slope-line-t-holds/) in the volume on analytic estimates: a family $\mathcal{D}$ of global data, a word $u$ of $\mathcal{D}$, the uniformizer $T = T_u$, the levels $0 \leq j \leq m$ with sizes $N_j$, the weights $\lambda_j(\tau)$ at the embeddings $\tau$, and the Hida setting for $u$. For Weyl modules see [highest weights](/learn/representations/#highest-weights-and-branching).

### The level-zero space

For a word $u$ let $\mathcal{C}_0$ be the finite set of classes at level $0$ and let $Y_0$ be the coefficient space. The *level-zero space* is the space $\mathcal{M}_0$ of functions $\varphi$ on $\mathcal{C}_0$ with $\varphi(c) \in Y_0(c)$. For a place $v$ over $T$ the *up operator* $U_v$ on $\mathcal{M}_0$ is the sum over the neighbours $x$ of each class $c$ (the lattices of the neighbouring level with the index condition $f_v(x) = 1$) of the transport map from $x$ to $c$; the *down operator* $D_v$ is the sum in the other direction. The *ramified part* $\mathcal{M}_0^{\mathrm{ram}} \subseteq \mathcal{M}_0$ is the subspace of functions that see only the ramified sublattice.

**Definition 7.9.1 (Concrete forms at level zero).** The *concrete forms at level zero* for $u$ are a tied symmetric system of forms whose character at level $0$ has finite order with values in the coefficient field, together with the condition that the stabilizers of the classes at level $0$ are trivial.

Two identities at level zero are the inputs of the Hecke relation. We take both from the theory of the diamond operators at one place.

**Theorem 7.9.2 (Matching of diamonds at one place).** For each system of forms at level zero, the up, down and transport operators at one place commute with the diamond operators at the same place.

**Theorem 7.9.3 (The $DU$ formula at level zero).** For each system of forms at level zero, each place $v$ over $T$ and each $\varphi$ in the space of forms,
$$D_v U_v \varphi = T^{N_0 - 1} \varphi - T^{N_0 - 2} N_v \varphi + T^{N_0 - 2}\, t_v \varphi,$$
where $N_v$ is the norm operator and $t_v$ is the transport operator at $v$.

**Theorem 7.9.4 (Hecke relation at a ramified place).** Let $u$ be a word of $\mathcal{D}$. Assume the Hida setting for $u$ and the concrete forms at level zero. Then for every place $v$ over $T$ and every $\varphi \in \mathcal{M}_0^{\mathrm{ram}}$,
$$U_v \varphi \in \mathcal{M}_0^{\mathrm{ram}}, \qquad D_v \varphi \in \mathcal{M}_0^{\mathrm{ram}}, \qquad U_v D_v \varphi = T^{N_0 - 1} \varphi.$$

Lean: `Formalism.L2.GlobalTheoryTheory.UnramifiedTrace.hecke_ramified_zero_all`.

*Proof.* The concrete forms give a system of forms at level zero, by restriction of the tied system to the level $0$. On it the up operator matches with the up operator of the neighbouring level, and the down operator matches at all places. The matching of diamonds at one place makes the up, down and transport operators commute with the diamond operators at $v$. The ramified part is defined through these operators, so it is stable under $U_v$ and $D_v$. The $DU$ formula, together with the transport identity that the matching of diamonds gives, then yields $U_v D_v \varphi = T^{N_0 - 1} \varphi$ on the ramified part. $\square$

### The second branch

Fix a place $w$ of the coefficient field over $T$ that is seen by $u$, and an embedding $\tau = \tau(w, v)$ attached to $w$ and a place $v$. Let $b = b_{\mathrm{top}}(\tau)$ be the top shift at $\tau$, let $S_0(w)$ be the level-zero lattice at $w$, let $B_{w,v} \subseteq S_0(w)$ be the lattice cut out by the Hecke operators at $v$, and let $t_L(b) \subseteq S_0(w)$ be the lattice of the forms divisible by $T^{b}$. Let $e_w$ be the ramification index of $w$, let $k$ be the parallel weight, and for a weight $\lambda$ let $\operatorname{wsum}(\lambda)$ be the sum of its entries.

Let $d(u)$ be the dimension count of the word $u$: the rank of the level-zero space that enters the length formulas of the family. For an integer $N$ and a weight $\lambda$ let $\Delta(N, \lambda)$ be the Weyl module of highest weight $\lambda$ for $GL_N$, realized as a module of polynomials over $\mathbb{Z}$.

**Theorem 7.9.5 (Second branch).** Let $u$ be a word of $\mathcal{D}$. Assume the Hida setting for $u$ and the concrete forms at level zero. Let $w$ be a seen place over $T$ and $v$ a place with $b = b_{\mathrm{top}}(\tau) \geq 0$, where $\tau = \tau(w, v)$. Then $t_L(b) \subseteq B_{w,v}$, and the length of the quotient is a natural number $n$ with
$$n = e_w \cdot \frac{d(u) \bigl(\operatorname{wsum}(\lambda_0(\tau)) + k\, b\bigr)}{k}.$$

Lean: `Formalism.L2.GlobalTheoryTheory.LemB.second_branch_all_members` (also `Formalism.L2.GlobalTheoryTheory.LemB.second_branch_of_rationality`, `Formalism.L2.GlobalTheoryTheory.LemB.second_branch_of_surjectivity` and `Formalism.L2.GlobalTheoryTheory.LemB.second_branch_of_coordinates_and_count`, the same conclusion from the inputs below).

The proof has three inputs. Let $\operatorname{RatSpan}$ be the span over the coefficient field of the rational forms, $\operatorname{CSpan}$ the span of the forms over $\mathbb{C}$, and $\operatorname{IntSpan}$ the span of the integral forms.

**Lemma 7.9.6 (Rational forms).** The rational span is contained in the complex span, and it is stable under the twisted substitution by each rational element $\gamma$ of the group.

**Definition 7.9.7 (Onto coordinates).** The forms at $(w, v)$ are *onto in coordinates* if the image of the integral span under the change of basis $b_{w}$ from level $N$ to level zero, scaled by $\det^{s}$ for the determinant shift $s$, is contained in the coordinates of $B_{w,v}$, and the scaled integral span is contained in the coordinates of $t_L(b)$.

**Lemma 7.9.8 (Weyl count formula).** For each word $u$,
$$d(u) = \#\mathcal{C}_0 \cdot \prod_{\tau} \operatorname{rk}_{\mathbb{Z}} \Delta(N_0, \lambda_0(\tau)).$$

Each class contributes one copy of the coefficient space, and the coefficient space is the tensor product over the embeddings of the Weyl modules.

*Proof of the theorem.* The first step gives surjectivity in coordinates. The lemma on rational forms says that each rational form is a complex form and that the twisted substitution preserves the rational span. So the integral span maps onto the coordinates of $B_{w,v}$ and of $t_L(b)$ under the basis change, which is the onto condition at every $(w, v)$.

The second step gives local bases. For each class $c$ at level $0$ there are local bases $B(c)$ of the level-zero lattice and $B'(c)$ of the lattice of forms at $v$, and the onto condition holds for them. The ratio of $\det(B^{-1} B')$ to the power of $T$ given by the determinant shift is a unit, by the second unramified condition and since a change of basis of one lattice has unit determinant. The onto condition then gives $t_L(b) \subseteq B_{w,v}$ in coordinates.

The third step computes the length. The length of $B_{w,v} / t_L(b)$ over the local ring of $w$ is the valuation of $\det(B^{-1} B')$, which is $e_w$ times the exponent over $T$. The exponent is the rank of the level-zero space times the weight $(\operatorname{wsum}(\lambda_0(\tau)) + k b) / k$, and the Weyl count formula identifies the rank with $d(u)$. $\square$

**Remark 7.9.9 (Formalization).** We did not open the definitions of the ramified part, the down operator, the lattices $B_{w,v}$ and $t_L(b)$, or the norm and transport operators; the descriptions above are our reading of their names and of the up operator ([DataLatDefs.lean](lean:Formalism/LocalRingCardinality/DataLatDefs.lean#L67)). We did not unfold how the $DU$ formula and the matchings combine in the Hecke proof. The Hecke relation from the matchings drops the Hida setting and the second half of the concrete forms ([HeckeRamifiedZeroOfMatchingsAndDu.lean](lean:Formalism/LocalToGlobal/GlobalTheory/UnramifiedDiagonal/HeckeRamifiedZeroOfMatchingsAndDu.lean#L30)). The second branch from coordinates and count also ignores the Hida setting ([SecondBranchOfCoordinatesAndCount.lean](lean:Formalism/LocalToGlobal/GlobalTheory/CoordinateLengths/SecondBranchOfCoordinatesAndCount.lean#L44)). The length formula is closed through a lemma at level zero that we did not open, so the third step of the proof is our reading of its inputs. The dimension count $d(u)$ is a field of the family data that we did not unfold. The rational and integral spans are defined three times, in TiedStep.lean, in Columns/TiedCF.lean and in ProductFirstZerothParts.lean.
