---
title: Uniformization of the base by balls
decls:
  - SheetDecomposition.baseUnifEx2
  - SheetDecomposition.baseUnifEx2_of
  - SheetDecomposition.kUnif_good
  - SheetDecomposition.univExists
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniformization of the base by balls

The volume theorem compares the volume of a good tower with a volume computed on the complex points of the moduli space. To compute volumes on the complex side, the complex points of the integral model must be written as a finite disjoint union of quotients of a product of complex balls by arithmetic groups. This section proves that such a base uniformization exists, with the extra property that a connected holomorphic family of points stays in one piece. The proof builds a universal family of Riemann lattices over the ball, uses the family uniformization of the moduli space at the embeddings with the right value on $\sqrt{-d_H}$, transports it to the conjugate embeddings, and glues. The result is used in the [volume equality](/entry/vol-eq-of-is-full-intersection-system/) of the next section.

We use the setting of [the chapter on good towers](/entry/good-tower-volume-of-reduced/): a CM field $E$ with host $H$, the set $\Psi$ of CM types of $H$, a datum $D$ of signature $(p, q)$, a level $l$, a family $X_o$ of moduli spaces, a coefficient field $c$ with field $F$, and an integral model $Y$ of $X_o(l)$ over the ring of integers of $F$.

**Definition 9.11.1 (Ball domain).** Let $j, j', n$ be natural numbers and $q \colon \Psi \times \{1, \dots, j\} \times \{1, \dots, j'\} \to \{1, \dots, n\}$ a bijection. For $t \in \mathbb{C}^n$ and $\tau \in \Psi$ let $Z_\tau(t)$ be the $j \times j'$ matrix with entries $t_{q(\tau, a, b)}$. The ball domain is

$$
\mathcal{B}_q = \{ t \in \mathbb{C}^n : 1 - Z_\tau(t)^* Z_\tau(t) \text{ is positive definite for all } \tau \}.
$$

The ball potential and the ball density are

$$
\begin{aligned}
\phi_q(t) &= -\sum_{\tau} \log \operatorname{Re} \det\big(1 - Z_\tau(t)^* Z_\tau(t)\big), \\
\rho_q(t) &= \exp\big((j + j') \phi_q(t)\big).
\end{aligned}
$$

So $\mathcal{B}_q$ is a product over $\Psi$ of bounded symmetric domains of $j \times j'$ matrices, and $\rho_q$ is the density of an invariant volume form on it.

A Riemann lattice of genus $g$ on an $\mathcal{O}_E$-module $\Lambda$ is a period map $P \colon \Lambda \to \mathbb{C}^g$, an integral alternating form, an action of $\mathcal{O}_E$ on $\mathbb{C}^g$ and a positive hermitian form, with the usual compatibilities. For a family $\sigma = (\sigma_\tau)$ of embeddings $\mathcal{O}_E \to \mathbb{C}$ that is a CM family, a Riemann lattice has signature $(j, j')$ if, for every $\tau$, the eigenspace of the action for $\sigma_\tau$ has dimension $j'$ and the eigenspace for the conjugate $\bar\sigma_\tau$ has dimension $j$.

**Definition 9.11.2 (Universal family).** A universal family on $\Lambda$ of type $(j, j', n, g)$ consists of a bijection $q$ as above, a CM family $\sigma$, an integral form, and Riemann lattices $R(t)$ for $t \in \mathbb{C}^n$, all with this form, such that:

1. $t \mapsto R(t)$ is holomorphic on $\mathcal{B}_q$ and $R(t)$ has signature $(j, j')$ for $\sigma$ for every $t \in \mathcal{B}_q$;
2. there are holomorphic frames $b_{\tau, i}(t)$, $i \le j'$, of the $\sigma_\tau$ eigenspaces whose log determinant is the ball potential $\phi_q(t)$;
3. every Riemann lattice $R'$ with the same form and signature $(j, j')$ for $\sigma$ is equivalent to $R(t)$, through the identity of $\Lambda$ and a $\mathbb{C}$-linear isomorphism of $\mathbb{C}^g$, for exactly one $t \in \mathcal{B}_q$.

For a subgroup $\Gamma$ of the $\mathcal{O}_E$-automorphisms of $\Lambda$, two points $t, t'$ are $\Gamma$-equivalent if $R(t)$ and $R(t')$ are equivalent through some $\gamma \in \Gamma$. The group is arithmetic for the family if it preserves the form and has finite index in the group of automorphisms that preserve the form.

**Definition 9.11.3 (Base uniformization).** Let $\mathrm{sm}$ be a map from CM types to labels and let $j, j', n$ be given. A base uniformization of $Y$ consists of a number $n_p$ of pieces and, for each piece $k$:

1. a datum $D_k$ with the signature $(p, q)$ of $D$ and an embedding $\kappa_k \colon F \to \mathbb{C}$;
2. a universal family $F_k$ on the lattice of $D_k$, with the same bijection $q$ for all $k$, with form $\pm$ the form of $D_k$, and with embeddings $\sigma_\tau = \kappa_k \circ \mathrm{label}(\mathrm{sm}(\tau))$;
3. the subgroup $\Gamma_k$ of automorphisms in the level of $D_k$, which is arithmetic for $F_k$;
4. a holomorphic map $\mathrm{pt}_k$ from $\mathcal{B}_q$ to the complex points of $Y$ over $\kappa_k$, with values in the abelian locus.

The pieces are disjoint: $\mathrm{pt}_k(t) = \mathrm{pt}_{k'}(t')$ implies $k = k'$. The fibres of $\mathrm{pt}_k$ are the $\Gamma_k$-equivalence classes. Every complex point of the abelian locus is some $\mathrm{pt}_k(t)$. The fibre of the abelian scheme at $\mathrm{pt}_k(t)$ has period lattice $R_k(t)$. Finally, for every Hodge component of $Y$ and every holomorphic lift of $\mathrm{pt}_k$ to it, the sections of the Lie lattice are given near each point by analytic vectors in the fibre lattices.

The base uniformization is locally constant if, for every preconnected open set $T \subseteq \mathbb{C}^m$ and every holomorphic family $y$ on $T$ of complex points of the abelian locus, whenever $y(b) = \mathrm{pt}_k(t)$ and $y(b') = \mathrm{pt}_{k'}(t')$ with $b, b' \in T$, we have $k = k'$.

So the complex points of the abelian locus are the disjoint union over $k$ of the quotients $\Gamma_k \backslash \mathcal{B}_q$, and a connected holomorphic family cannot jump between pieces. This is the classical uniformization of a unitary Shimura variety by a product of complex balls.

**Theorem 9.11.4 (Universal families exist).** Let $\sigma$ be a CM family, $q$ a bijection as above, and $R_0$ a Riemann lattice on $\Lambda$ of signature $(j, j')$ for $\sigma$. Then there is a universal family on $\Lambda$ with bijection $q$, embeddings $\sigma$ and the form of $R_0$.

Lean: `SheetDecomposition.univExists`

*Proof.* Choose a frame of $\mathbb{C}^g$, orthonormal for the hermitian form of $R_0$ and adapted to the eigenspaces of $\sigma$; it gives a normalized Riemann lattice $R_1$ with the same form whose hermitian form is the identity and whose action is diagonal. For $t \in \mathcal{B}_q$ let $Z(t)$ be the block matrix built from the $Z_\tau(t)$. The Siegel transform by $Z(t)$ gives a Riemann lattice $R(t)$ with the same form, the same action, hermitian form $(1 - Z(t)^* Z(t))^{-1}$, and period map $P_{R(t)} = T_{Z(t)} \circ P_{R_1}$; this is possible since $t \in \mathcal{B}_q$ makes $1 - Z(t)^* Z(t)$ positive definite and the transform commutes with the action. Outside $\mathcal{B}_q$ put $R(t) = R_1$.

The period maps are holomorphic in $t$ since $T_{Z(t)}$ is. The eigenspaces are spanned by standard basis vectors, which gives the signature and constant frames $b_{\tau, i}$. The log determinant of these frames for the hermitian form $(1 - Z^* Z)^{-1}$ is the ball potential. For universality, let $R'$ have the same form and signature. A real extension identifies $R'$ with $R_1$ on the underlying real space, and the Siegel normal form of the hermitian form of $R'$ gives a matrix $Z$ and an isomorphism $A$ with $R'$ the transform of $R_1$ by $Z$ up to $A$. The criterion for conjugate embeddings shows that $Z$ has the block shape of some $Z(t)$, and positivity puts $t$ in $\mathcal{B}_q$. Uniqueness of $t$ follows from the uniqueness of the transform. $\square$

The next theorem works at one embedding $\kappa$ of $F$. A $\kappa$-uniformization is a base uniformization in which all pieces lie over the same embedding $\kappa$, the index set is any finite type, the bijection is a fixed $q$, every complex point of the abelian locus over $\kappa$ is reached, and local constancy holds for families over $\kappa$.

**Theorem 9.11.5 (Uniformization at good embeddings).** Assume the vector statement for periods. Let $\mathrm{sm}$, $j$, $j'$ satisfy $(\mathrm{sm}, j, j') = (\mathrm{right}, p, q)$ or $(\mathrm{left}, q, p)$, let $\rho \in F$ be the square root of $-d_H$ that maps to the fixed root $r_0$ in $\mathbb{C}$, and let $\kappa \colon F \to \mathbb{C}$ satisfy $\kappa(\rho) = r_0$. Given a family uniformization of $X_o$ at the restriction of $\kappa$, there is a $\kappa$-uniformization of $Y$ with bijection $q$.

Lean: `SheetDecomposition.kUnif_good`

*Proof.* The pieces are the pieces $i$ of the family uniformization that carry at least one period. For such a piece, a period gives a Riemann lattice on the lattice of $D_i$ with the form of $D_i$, and its signature in the sense of the family uniformization is signature $(j, j')$ for the embeddings $\kappa \circ \mathrm{label}(\mathrm{sm}(\tau))$; this is where $\kappa(\rho) = r_0$ and the choice of $(\mathrm{sm}, j, j')$ enter. The theorem on universal families gives a universal family $F_i$ with bijection $q$ and the form of $D_i$. Since the level has $M \ge 3$ and $A > 0$, the automorphisms of the form in the level form an arithmetic congruence subgroup $\Gamma_i$.

Near each point of $\mathcal{B}_q$ the period maps of $F_i$ are, up to a holomorphic invertible matrix, a holomorphic family of periods. The family uniformization sends a period to a complex point of $X_o$; equivalent periods have the same image, so the image depends only on $R_i(t)$. Together with $\kappa$ this gives points of the base change of $X_o$ to $F$ and then, through the map to $Y$, the points $\mathrm{pt}_i(t)$. They are holomorphic, lie over $\kappa$ and lie in the abelian locus.

The axioms follow from those of the family uniformization. Disjointness and the description of the fibres are its disjointness and fibre statements, with the level conditions translated into membership in $\Gamma_i$. A point of the abelian locus over $\kappa$ comes from a point of the base change, which the family uniformization reaches by some period; universality gives the parameter $t$. The lattice condition is the period lattice statement for the family uniformization, moved to $Y$ by two base changes. The vector condition is the vector statement for periods applied on the open sets where the local holomorphic periods exist. Local constancy follows since a preconnected holomorphic family of points of the base change stays in one piece of the family uniformization. $\square$

**Theorem 9.11.6 (Assembly).** The vector statement for periods and the conjugation statement for $\kappa$-uniformizations imply the existence statement: assume the top level inputs, let $p + q \ge 1$, let $(\mathrm{sm}, j, j')$ be $(\mathrm{right}, p, q)$ or $(\mathrm{left}, q, p)$, and let $n = |\Psi|\, j\, j'$. Then $Y$ has a locally constant base uniformization.

Lean: `SheetDecomposition.baseUnifEx2_of`

*Proof.* The top level inputs contain the statement that $X_o$ has a family uniformization at every embedding $\sigma$ of the base field with $\sigma(\rho) = r_0$, for a type function of signature $(p, q)$; a type function exists. Since $n = |\Psi|\, j\, j'$, there is a bijection $q$. By the previous theorem, there is a $\kappa$-uniformization for every $\kappa$ with $\kappa(\rho) = r_0$.

Let $\kappa$ be any embedding of $F$. Since $\rho^2 = -d_H$, we have $\kappa(\rho) = \pm r_0$. If $\kappa(\rho) = -r_0$, then the conjugate embedding $\bar\kappa$ has $\bar\kappa(\rho) = r_0$, so $\bar\kappa$ has a $\kappa$-uniformization, and the conjugation statement gives one for $\bar{\bar\kappa} = \kappa$. So every embedding has one.

Glue them. The pieces are the pairs $(\kappa, k)$ with $k$ a piece of the uniformization at $\kappa$; there are finitely many, and we number them. A point determines its embedding, since the structure map of $Y$ at a complex point is induced by a unique embedding of $F$; so pieces over different embeddings are disjoint, and every point of the abelian locus is reached in the uniformization at its own embedding. For local constancy, the embedding attached to $y(b)$ is holomorphic in $b$ and takes values in a discrete set, so it is constant on the preconnected set $T$; then local constancy at that embedding applies. $\square$

**Theorem 9.11.7 (Base uniformization).** Assume the top level inputs. Let $p + q \ge 1$, let $(\mathrm{sm}, j, j')$ be $(\mathrm{right}, p, q)$ or $(\mathrm{left}, q, p)$, and let $n = |\Psi|\, j\, j'$. Then $Y$ has a locally constant base uniformization of type $(\mathrm{sm}, j, j', n)$.

Lean: `SheetDecomposition.baseUnifEx2`

*Proof.* The vector statement for periods follows from the statement on holomorphic coordinates, and the conjugation statement for $\kappa$-uniformizations holds: conjugating a universal family and composing the points with complex conjugation gives a uniformization at the conjugate embedding. The assembly theorem then applies. $\square$

The two choices of $(\mathrm{sm}, j, j')$ correspond to the two ways of writing the signature: the balls of $j \times j'$ matrices for the right labels with $(p, q)$, or the transposed balls for the left labels with $(q, p)$. The volume equality uses the first.

**Remark 9.11.8 (Formalization).** The family uniformization statement is taken from the top level inputs by position, as a part of the first part ([BaseUnifAsm.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/BaseUnifAsm.lean#L104)). The development also contains a theorem `GlobalTheory.T.cmModuli_consequence_of_abelianSchemeLaws` with exactly this statement and no hypotheses, so this part of the top level inputs could be removed; we have not checked the proof behind that theorem. The universal family theorem is a second name for a theorem in a sub-namespace ([BaseUnifUnivC.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/BaseUnifUnivC.lean#L283)). Next to the main theorem there is a weaker form that forgets local constancy ([BaseUnif.lean](lean:Development/WeilBound/CoreStatements/VolumeEquality/BaseUnif.lean#L10)). The proof of universality is described by its steps; we have not unfolded the Siegel transform, the real extension, the criterion for conjugate embeddings, the fibre lattice conditions, or the vector statement for periods. The reading of $\mathcal{B}_q$ as a product of bounded symmetric domains and of $\rho_q$ as an invariant density is ours.
