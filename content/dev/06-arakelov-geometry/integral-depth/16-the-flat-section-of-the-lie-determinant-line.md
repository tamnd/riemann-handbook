---
title: The flat section of the Lie determinant line
decls:
  - GlobalTheory.DetLine.exists_of_snc
  - GlobalTheory.DetLine.detLineTrivial_of_toroidal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The flat section of the Lie determinant line

Let $A$ be the universal abelian scheme with multiplication by $\mathcal{O}_E$ over a moduli space of signature $(p, q)$. Its Lie algebra splits into the eigenparts of a character $\chi$ and of its conjugate $\bar\chi$, of ranks $p$ and $q$. The line $(\det \mathrm{Lie}_\chi)^{-1} \otimes \det \mathrm{Lie}_{\bar\chi}$ is trivial on each geometrically connected component of the generic fibre. This section proves this in a strong form: the line has a nowhere vanishing section that is flat for the complex uniformization, unique up to a constant, and it extends without zeros to every normal compactification. The result is used in [the covolume of the top lattice](/entry/top-covol-g-alt-alt/), where the flat section turns a ratio of lattice volumes into a constant ([Shimura varieties and toroidal compactifications](/learn/geometry/#shimura-varieties-and-toroidal-compactifications)).

We use the moduli data of the previous sections: a CM field $E$ with host data $H$, a datum $\mathcal{D}$ of signature $(p, q)$, a level, a moduli space $X_o$ with coefficients $c$ in a field $F$, the generic fibre $X_{o,F}$ and the universal semiabelian scheme over $X_o$ with its $\mathcal{O}_E$-action. Fix an embedding $\tau : E \to \mathbb{C}$ with $\tau(\varrho) = \varrho_0$, and let $\chi : \mathcal{O}_E \to F$ be the character defined by $\tau$.

**Definition 3.16.1 (Lie frames and rules).** Let $V \subset X_{o,F}$ be a set. Let $R$ be a ring with a map $j : F \to R$ and $x$ an $R$-point of $X_{o,F}$ over $j$ with image in $V$. A *Lie frame* at $x$ is a pair $(v, w)$, where $v = (v_1, \dots, v_p)$ is a basis of the $\chi$-eigenpart and $w = (w_1, \dots, w_q)$ a basis of the $\bar\chi$-eigenpart of the Lie algebra of the universal scheme at $x$. Tangent vectors are maps from the first order thickening of $x$ to the group. A *rule* $\sigma$ assigns to every such $(R, x, v, w)$ an element $\sigma(x, v, w) \in R$. A rule is a *section* on $V$ if:

1. it commutes with base change along every ring map $R \to R'$;
2. if $v' = M v$ and $w' = N w$ for invertible matrices $M$ and $N$, then
$$\det N \cdot \sigma(x, v, w) = \det M \cdot \sigma(x, v', w').$$

It is *nowhere zero* if every value is a unit, and $\sigma'$ is the *multiple* $a \sigma$ for $a \in F$ if $\sigma'(x, v, w) = j(a)\sigma(x, v, w)$ for all frames.

Condition 2 says that $\sigma(x, v, w)$ changes by $(\det M)^{-1} \det N$. So a section is the same as a section of the line $(\det\mathrm{Lie}_\chi)^{-1} \otimes \det\mathrm{Lie}_{\bar\chi}$ on $V$, written as a function on frames.

**Definition 3.16.2 (Transport and flatness).** Let $e : F \to \mathbb{C}$ be an embedding and $y$ a complex point of $X_{o,F}$ over $e$. The abelian variety at $y$ has a holomorphic uniformization $\mathbb{C}^g / \Lambda$ with a hermitian form $H_y$ and the $\mathcal{O}_E$-action and level structure on $\mathbb{C}^g$. For two complex points $y$, $y'$ over $e$, a *transport* is an $\mathbb{R}$-linear isomorphism $\varphi : \mathbb{C}^g \to \mathbb{C}^{g'}$ that maps $\Lambda$ onto $\Lambda'$, commutes with the $\mathcal{O}_E$-action, keeps the imaginary part of the hermitian form, and keeps the level structures. *Transport exists at $e$* on $V$ if any two complex points of $V$ over $e$ have a transport between their uniformizations.

For a Lie frame $(v, w)$ at $y$ with coordinates $V_1, \dots, V_p$ and $W_1, \dots, W_q$ in $\mathbb{C}^g$ and a family $x = (x_k)$ of $p + q$ vectors, the *period determinant* is
$$\Delta = \det\begin{pmatrix} -\pi H_y(W_j, x_k) & a_{k i} \end{pmatrix}_{k},$$
where $x_k - \sum_i a_{k i} V_i$ is $H_y$-orthogonal to all $V_i$. A rule $\sigma$ is *flat at $e$* if for all complex points $y$, $y'$ over $e$ in $V$, all frames, all transports $\varphi$ and all families $x$,
$$\sigma(y, v, w)\, \Delta' = \sigma(y', v', w')\, \Delta,$$
where $\Delta'$ is the period determinant at $y'$ for the family $\varphi(x)$.

Flatness says that the ratio of $\sigma$ and the period determinant does not change under transport. Since the period determinant changes with the frame in the same way as a section, the ratio is a function on the points.

**Definition 3.16.3 (Trivial determinant line).** The *trivial determinant line statement* says: for all moduli data as above, every open and closed set $U \subset X_{o,F}$ that is geometrically connected over $F$, and every $\tau$ with $\tau(\varrho) = \varrho_0$:

1. transport exists on $U$ at every embedding $e : F \to \mathbb{C}$;
2. there is a section $\sigma$ on $U$ that is nowhere zero and flat at every $e$;
3. every section $\sigma'$ on $U$ that is flat at every $e$ is $a\sigma$ for a unique $a \in F$;
4. for every ring $O$ with a map $\beta : O \to F$ and every model $Y$ of $X_o$ over $O$ whose base change $Y_F$ is normal, there is a nowhere zero section $\sigma_b$ on the closure $\bar U$ of $U$ in $Y_F$ that restricts to $\sigma$ on $U$, and every section on $\bar U$ is $a\sigma_b$ for a unique $a \in F$.

We say that the data have a *flat section* if parts 1 and 2 hold and, in part 4, a nowhere zero section $\sigma_b$ that restricts to $\sigma$ exists.

**Lemma 3.16.4 (Flat section from a smooth compactification).** Let $Z$ be a model of $X_o$ over a ring $O$ with a map $\beta : O \to F$ whose generic part is smooth of relative dimension $\dim\mathcal{D}$ and whose boundary is a divisor with simple normal crossings. Let $U$ be open, closed and geometrically connected, let $\tau(\varrho) = \varrho_0$, and assume $p + q \ge 1$. Then the data have a flat section.

Lean: `GlobalTheory.DetLine.exists_of_snc`.

*Proof.* We follow the construction in five steps; each step is an input lemma proved in the development. Call an embedding $e : F \to \mathbb{C}$ *good* if it maps the root of the base field to $\varrho_0$. For every $e$, either $e$ or its complex conjugate $\bar e$ is good, since the two values are square roots of the same number and $\varrho_0$ is purely imaginary.

1. *Compactify the component.* An input lemma gives a variety that compactifies the component $U$ inside the generic part of $Z$.
2. *Good embeddings.* At a good embedding $e$, the laws of abelian schemes give a family of complex abelian varieties over the component, and each member has a basis of its hermitian period lattice of the same signature.
3. *A nowhere vanishing section.* At one good embedding, a horizontal function built from these period bases gives a nowhere vanishing section $\sigma_Z$ of the determinant line on $Z$. Its restriction to $U$ is a nowhere zero section $\sigma$ on $U$.
4. *Transport and flatness.* At a good embedding $e$, transport exists by the CM type of the family, and $\sigma_Z$ is a constant multiple of the horizontal coordinate of the Lie determinant, which is the period determinant; so $\sigma$ is flat at $e$. At an embedding $e$ that is not good, $\bar e$ is good, and transport and flatness at $e$ follow from those at $\bar e$ by complex conjugation.
5. *Extension.* The section $\sigma_Z$ gives a nowhere zero extension of $\sigma$ to every normal compactification $\bar U \subset Y_F$. $\square$

**Theorem 3.16.5 (Flat section of the Lie determinant line).** Assume the existence of toroidal compactifications of the moduli spaces, with smooth total space and simple normal crossings boundary. Then the trivial determinant line statement holds.

Lean: `GlobalTheory.DetLine.detLineTrivial_of_toroidal`.

*Proof.* Fix the data.

*Existence.* If $p + q = 0$, the frames are empty, all determinants are $1$, and the rule $\sigma = 1$ is a nowhere zero flat section. An input lemma on rank zero gives the transport, and the rule $\sigma_b = 1$ on each normal compactification is a nowhere zero section that restricts to $\sigma$. If $p + q \ge 1$, the assumption gives a model $Z$ with a smooth generic part of relative dimension $\dim\mathcal{D}$ and a boundary with simple normal crossings. Smoothness passes to the base change, and the boundary ideal of the generic part has simple normal crossings. [The previous lemma](/entry/exists-of-snc/) gives a flat section. This proves parts 1, 2 and the existence in part 4.

*Uniqueness on $U$.* Let $\sigma'$ be a section on $U$ that is flat at every $e$. Fix the embedding $e_0 : F \subset \mathbb{C}$. At complex points over $e_0$, the ratio $\sigma'/\sigma$ is a function on points, since both change in the same way with the frame. Flatness of both and the existence of transport between any two points show that the ratio is the same at all complex points over $e_0$. Since $U$ is geometrically connected and $\sigma$ is nowhere zero, the ratio is a constant $a \in F$, and it is unique.

*Uniqueness on $\bar U$.* Let $\sigma'$ be a section on $\bar U$. The ratio $\sigma'/\sigma_b$ is a regular function on $\bar U$, since $\sigma_b$ is nowhere zero. An input lemma says that a regular function on a normal compactification of a geometrically connected $U$ is a constant in $F$. So $\sigma' = a\sigma_b$ with a unique $a$. $\square$

The uniqueness on $\bar U$ does not need flatness: on the compactification, regularity alone fixes the section up to a constant. On $U$ itself the ratio of two sections could be any invertible function, and flatness is what makes it constant.

**Remark 3.16.6 (Formalization).** The existence of toroidal compactifications is a published hypothesis, and it is used only when $p + q \ge 1$ ([DetLineTrivialOfToroidal.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DetLineTrivialOfToroidal.lean#L182)). The uniqueness on $U$ uses flatness only at the given embedding of $F$ into $\mathbb{C}$. The statement is called a trivial determinant line, but it is phrased with rules on frames, not with a line bundle ([HermitianCompactForm.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/HermitianCompactForm.lean#L163)); a second definition with the same name is in `FramedFlatCoordinates.lean` at line 185, and the theorem proves the one in `HermitianCompactForm.lean`. We have not unfolded the uniformizations, the level structures, the models and the inputs of the construction; the five steps of the lemma describe these inputs by their role.
