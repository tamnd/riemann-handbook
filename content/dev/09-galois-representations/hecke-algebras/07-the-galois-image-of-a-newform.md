---
title: The Galois image of a newform
decls:
  - GlobalTheory.KZ.HeckeProj.heckeProj_main
  - GlobalTheory.T.galois_representation_of_eigensystem
  - GlobalTheory.KZ.HeckeProj.heckeProj_newform
  - GlobalTheory.T.heckeProjector_newform_galoisImage
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Galois image of a newform

This section puts the last three sections together. Let $g$ be a newform of odd weight $k \geq 3$ and let $\rho$ be an irreducible two dimensional Galois representation whose Frobenius traces and determinants match the Hecke eigenvalues of $g$. We show that a polynomial $P$ in the Hecke operators projects the Kummer module of [the previous section](/entry/eichler-shimura-frobenius-quadratic-mod-prime-pow/) onto its $g$-eigenspace, and that this eigenspace is a finite direct sum of copies of $\rho$, with explicit projections and inclusions. This is the form in which the Galois representation of $g$ enters the Euler system argument: [the admissible functional on the tower](/entry/kato-global-admissibility-of-admissible/) uses it to move from Kummer classes of modular units to classes with values in $\rho$.

We keep the notation of the last section: a tower $(K, \dots)$ over $(\Omega, \varepsilon)$, a prime $l \neq 2$, a level $N \geq 5$ with $\gcd(N, l) = 1$, an odd weight $w$, the Kummer module $\mathcal{B}$, and a field $E$ that is algebraically closed, has an absolute value, and receives $\mathbb{Z}_l$ by a map that preserves the absolute value. Let $\mathcal{B}_E \subseteq E \otimes_{\mathbb{Z}_l} \mathcal{F}$ be the image of $E \otimes \mathcal{B}$. For a letter $T$ and $s \in \mathrm{Gal}(\Omega/\mathbb{Q})$ we write $T$ and $s_*$ also for their base changes to $E \otimes \mathcal{F}$.

**Definition 6.7.1 (Semisimple projector on the Kummer module).** An eigensystem $\lambda$ with values in $E$ has a *semisimple projector on $\mathcal{B}_E$* if there is $P \in \mathcal{A}_E$ with $\lambda(P) = 1$ such that
$$
(T - \lambda(T))(P x) = 0
$$
for every $x \in \mathcal{B}_E$ and every admitted letter $T$.

This is the analogue of the semisimple projector on potentials of [Section 6.5.4](/entry/ss-pot-b-at-newform/), with "trivial" replaced by "zero". A comparison theorem of the development transfers the first to the second: if $\iota : E \to \mathbb{C}$ is a field isomorphism and $\iota \circ \lambda$ has a semisimple projector on potentials of weight $w$, then $\lambda$ has a semisimple projector on $\mathcal{B}_E$.

**Definition 6.7.2 (Galois representation with the eigenvalues of $\lambda$).** Let $\lambda$ be an eigensystem with values in $E$. A *Galois representation for $\lambda$* is a group homomorphism $\rho : \mathrm{Gal}(\Omega/\mathbb{Q}) \to \mathrm{GL}_2(E)$ together with a finite set $S_0$ of primes such that:

1. the maps $s \mapsto \operatorname{tr}\rho(s)$ and $s \mapsto \det\rho(s)$ are uniformly continuous, in the sense of [the Cayley and Hamilton theorem](/entry/cayley-hamilton-gal-v/);
2. for every prime $q \notin S_0$ and every Frobenius $s$ at $q$,
$$
\operatorname{tr}\rho(s) = \lambda(T_q), \qquad \det\rho(s) = q^{w+1}\lambda(\langle q \rangle);
$$
3. $\rho$ is irreducible: the only subspaces of $E^2$ stable under all $\rho(s)$ are $0$ and $E^2$.

These are the conditions satisfied by the [Galois representation of a newform](/learn/galois-representations/#the-galois-representation-of-an-automorphic-representation) of weight $w + 2$, with $\lambda(T_q) = a_q$ and $\lambda(\langle q \rangle) = \chi(q)$, after a choice of isomorphism between $\overline{\mathbb{Q}}_l$ and $\mathbb{C}$.

We use one fact from linear algebra.

**Lemma 6.7.3 (Representations with a quadratic relation).** Let $E$ be an algebraically closed field of characteristic not $2$, let $G$ be a group, and let $\rho : G \to \mathrm{GL}_2(E)$ be irreducible. Let $U$ be a finite dimensional $E$-vector space with a representation $\sigma$ of $G$ such that
$$
\sigma(g)^2 - \operatorname{tr}\rho(g)\, \sigma(g) + \det\rho(g) = 0 \qquad \text{for all } g \in G.
$$
Then there are $m \geq 0$ and linear maps $\pi_i : U \to E^2$, $\iota_i : E^2 \to U$ for $i = 1, \dots, m$ with $\pi_i \sigma(g) = \rho(g) \pi_i$, $\sigma(g) \iota_i = \iota_i \rho(g)$, $\pi_i \iota_j = \delta_{ij}$ and $\sum_i \iota_i \pi_i = 1$. That is, $U \cong (E^2)^m$ as a representation.

The idea is that, by Burnside's theorem, $\rho$ maps the group algebra $E[G]$ onto $M_2(E)$, and the quadratic relation forces the action of $E[G]$ on $U$ to factor through this map. Then $U$ is a module over the simple algebra $M_2(E)$, and so a direct sum of copies of $E^2$.

**Theorem 6.7.4 (Galois representation on an eigensystem).** Let $\lambda$ be an eigensystem with values in $E$ that has a semisimple projector on $\mathcal{B}_E$, and let $(\rho, S_0)$ be a Galois representation for $\lambda$. Then there are $m \geq 0$, linear maps $\pi_i : E \otimes \mathcal{F} \to E^2$ and $\iota_i : E^2 \to E \otimes \mathcal{F}$ for $i = 1, \dots, m$, and $P \in \mathcal{A}_E$ with $\lambda(P) = 1$, such that:

1. $\sum_i \iota_i \pi_i x = x$ for every $x \in \mathcal{B}_E$ with $T x = \lambda(T) x$ for all admitted $T$;
2. $\iota_i v \in \mathcal{B}_E$ for all $i$ and $v \in E^2$;
3. $\pi_i(s_* x) = \rho(s) \pi_i x$ for $x \in \mathcal{B}_E$, and $s_*(\iota_i v) = \iota_i(\rho(s) v)$ for $v \in E^2$;
4. $T(\iota_i v) = \lambda(T)\iota_i v$ and $\pi_i(T x) = \lambda(T)\pi_i x$ for admitted $T$, $v \in E^2$ and $x \in \mathcal{B}_E$;
5. $\pi_i \iota_j = \delta_{ij}$;
6. $P x = \sum_i \iota_i \pi_i x$ for $x \in \mathcal{B}_E$.

Lean: `GlobalTheory.KZ.HeckeProj.heckeProj_main` (also `GlobalTheory.T.galois_representation_of_eigensystem`, a second name).

*Proof.* Let $P$ be the semisimple projector for $\lambda$.

*Stability.* The space $\mathcal{B}_E$ is finite dimensional, as $\mathcal{B}$ is free of finite rank. It is stable under every $s_*$ and every admitted letter, and these commute on it, because the same holds for $\mathcal{B}$ and these properties pass to the base change. So the operator $P$ maps $\mathcal{B}_E$ into itself and commutes with every $s_*$ there.

*The eigenspace.* Let $U = P(\mathcal{B}_E)$. By the choice of $P$, every $u \in U$ satisfies $T u = \lambda(T) u$ for all admitted $T$. Conversely, if $y$ satisfies these equations, then $P y = \lambda(P) y = y$, since $P$ is a polynomial in the admitted letters. So $U$ is the joint eigenspace of the admitted letters in $\mathcal{B}_E$, and $P$ is the identity on $U$. As $P$ commutes with $s_*$, the space $U$ is stable under every $s_*$. The maps $s \mapsto s_*$ form a group homomorphism, so we get a representation $\sigma$ of $\mathrm{Gal}(\Omega/\mathbb{Q})$ on $U$.

*The quadratic relation.* For $u \in U$, [the Cayley and Hamilton theorem](/entry/cayley-hamilton-gal-v/) with $t = \operatorname{tr}\rho$ and $d = \det\rho$ gives $\sigma(s)^2 u - \operatorname{tr}\rho(s)\, \sigma(s) u + \det\rho(s)\, u = 0$. The field $E$ has characteristic not $2$, since $|2| = |2|_l \neq 0$.

*Decomposition.* The lemma gives maps $\pi'_i : U \to E^2$ and $\iota_i : E^2 \to U$ with the stated properties on $U$. Put $\pi_i = \pi'_i \circ P$ on $\mathcal{B}_E$, and extend it linearly to all of $E \otimes \mathcal{F}$ in any way. Then property 6 follows from $\sum_i \iota_i \pi'_i = 1$ on $U$, property 1 from $P y = y$ on eigenvectors, and properties 3 and 4 from the fact that $P$ commutes with $s_*$ and with the admitted letters on $\mathcal{B}_E$. Property 5 holds because $P$ is the identity on $U$. $\square$

The maps $\pi_i$ are only fixed on $\mathcal{B}_E$, and only properties of $\pi_i$ on $\mathcal{B}_E$ are claimed. Off $\mathcal{B}_E$ they are an arbitrary extension.

**Theorem 6.7.5 (Hecke projector for a newform).** Let $k \geq 3$ be odd and let $g$ be a newform of weight $k$, level $M$ and character $\chi$, with coefficients $a_n$. Let $N \geq 5$ with $M \mid N$, let $l \neq 2$ be a prime with $\gcd(N, l) = 1$, and let $\alpha \in \mathbb{C}$ with
$$
\alpha^2 - a_l \alpha + \chi(l) l^{k-1} = 0, \qquad \alpha^2 \neq \chi(l) l^{k-1}, \qquad \alpha^2 \neq \chi(l) l^{k-2}.
$$
Let $\lambda_{\mathbb{C}}$ be an eigensystem with $\lambda_{\mathbb{C}}(T_q) = a_q$ for primes $q \nmid Nl$, $\lambda_{\mathbb{C}}(U) = \alpha$, and $\lambda_{\mathbb{C}}(\langle d \rangle) = \chi(d)$ for $d$ prime to $N$. Let $E$ be as above, let $\iota : E \to \mathbb{C}$ be a field isomorphism, and put $\lambda = \iota^{-1} \circ \lambda_{\mathbb{C}}$ and $w = k - 2$. Let $(\rho, S_0)$ be a Galois representation for $\lambda$. Then the conclusion of the last theorem holds for $\lambda$ and $\rho$.

Lean: `GlobalTheory.KZ.HeckeProj.heckeProj_newform` (also `GlobalTheory.T.heckeProjector_newform_galoisImage`, a second name).

*Proof.* By [the Hecke projector on potentials](/entry/ss-pot-b-at-newform/), $\lambda_{\mathbb{C}} = \iota \circ \lambda$ has a semisimple projector on potentials of weight $k - 2$. The weight $w = k - 2$ is odd, as $k$ is odd. By the comparison theorem quoted above, $\lambda$ has a semisimple projector on $\mathcal{B}_E$. The last theorem then gives the conclusion. $\square$

An isomorphism $\iota$ exists for $E = \mathbb{C}_l$, the completion of an algebraic closure of $\mathbb{Q}_l$, since both fields are algebraically closed of characteristic $0$ with the same uncountable cardinality. No continuity of $\iota$ is asked, and none is used. The irreducibility of $\rho$ is used only through the lemma on quadratic relations.

**Remark 6.7.6 (Formalization).** Both theorems assume that $\varepsilon$ is injective and that the germ of $j_K$ is holomorphic ([HeckeProjectorNewformGaloisImage.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/HeckeProjectorNewformGaloisImage.lean#L12), [GaloisRepresentationOfEigensystem.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GaloisRepresentationOfEigensystem.lean#L133)); both are automatic, as in Section 6. The file of the main theorem raises `maxHeartbeats` to 1600000 ([GaloisRepresentationOfEigensystem.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/GaloisRepresentationOfEigensystem.lean#L12)), and a helper lemma ends in a `first` with six alternatives. The semisimple projector on $\mathcal{B}_E$ has three copies with the same body, `SSB` ([OpLDOneSubMemTriv.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/OpLDOneSubMemTriv.lean#L65)), `SSBB` ([LiftApplyOfMemAdmissibleSubalgebra.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/LiftApplyOfMemAdmissibleSubalgebra.lean#L21)) and `SSBA`, linked by `Iff.rfl`. The maps $\pi_i$ are extended off $\mathcal{B}_E$ by an arbitrary choice. The lemma on quadratic relations and the comparison theorem between potentials and the Kummer module were read as statements; the sketch of the lemma above is the standard argument.
