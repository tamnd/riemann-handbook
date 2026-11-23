---
title: An integral model of Harris-Taylor type
decls:
  - GlobalTheory.UPel.HT.model_nonempty
  - GlobalTheory.T.exists_quasiProjective_harrisTaylor_family
  - GlobalTheory.UPel.HT.exists_repFam_qproj
status: drafted
drafted_by: writer@claude-opus-5-5
---
## An integral model of Harris-Taylor type

This section proves that a moduli problem of abelian schemes with polarization, endomorphisms and level structure (a PEL moduli problem) of the type that Harris and Taylor use has a smooth quasi-projective fine moduli scheme over every noetherian ring in which the integers prime to $p$ are units. For PEL problems in general this is due to Kottwitz (J. Amer. Math. Soc. 5 (1992), §5), and Harris and Taylor set up their models in Chapter III of *The geometry and cohomology of some simple Shimura varieties* (Annals of Math. Studies 151, 2001). We have not checked the datum below against Harris and Taylor. The proof here has the usual form. One adds an auxiliary symplectic level structure of odd prime level $M$, maps the problem to a Siegel moduli problem, which is representable by geometric invariant theory (Mumford, Fogarty and Kirwan, *Geometric Invariant Theory*, Chapter 7), and then removes the auxiliary level. The result goes into the [package of facts about the Kuga-Sato tower](/entry/kodaira-spencer-of-weight-one/) of the Galois row.

### The moduli problem

Let $p$ be a prime.

**Definition 8.1.1 (Datum).** A *datum* $D$ for $p$ consists of the following.

1. A CM field $F$ with complex conjugation $c \mapsto \bar{c}$, which restricts to a ring automorphism of $\mathcal{O}_F$, and $\omega \in \mathcal{O}_F$ with $\omega + \bar{\omega} = t_0$ and $\omega \bar{\omega} = n_0$ for integers $t_0, n_0$ such that $t_0^2 - 4n_0 < 0$, $p \nmid t_0^2 - 4n_0$, and $p \mid r^2 - t_0 r + n_0$ for some $r \in \mathbb{Z}$.
2. A ring $O$ with an $\mathcal{O}_F$-algebra structure, free of rank $m^2 [F : \mathbb{Q}]$ over $\mathbb{Z}$ with $m \geq 1$, such that a nonzero integer multiple of every central element lies in the image of $\mathcal{O}_F$. An anti-automorphism $*$ of $O$ of order $2$ that is $c \mapsto \bar{c}$ on $\mathcal{O}_F$, and an isomorphism of $\mathcal{O}_F$-algebras $O \otimes \mathbb{Z}_p \cong M_m(\mathcal{O}_F \otimes \mathbb{Z}_p)$.
3. An $O$-module $\Lambda$, free of rank $mn[F : \mathbb{Q}]$ over $\mathbb{Z}$ with $n \geq 1$, and an alternating form $E : \Lambda \times \Lambda \to \mathbb{Z}$ such that $x \mapsto E(x, -)$ is injective and $E(bx, y) = E(x, b^* y)$. There is an integer $e$ prime to $p$ such that for every linear form $f : \Lambda \to \mathbb{Z}$ there is $x \in \Lambda$ with $E(x, -) = e f$.
4. An integer $a \geq 0$, a root $\rho_{\mathbb{C}}$ of $X^2 - t_0 X + n_0$ in $\mathbb{C}$, and distinct embeddings $\tau_1, \dots, \tau_a : F \to \mathbb{C}$ with $\tau_i(\omega) = \rho_{\mathbb{C}}$. A complex structure $J$ on $\Lambda_{\mathbb{R}}$ that preserves $E$, is positive for $E$, commutes with $O$, and satisfies a trace condition for the action of $\mathcal{O}_F$, given by $a$, $m$, $n$ and the $\tau_i$.

Lean: `GlobalTheory.UPel.HT.Datum`.

**Definition 8.1.2 (Base).** A *base* $b$ for $D$ over a ring $R$ consists of a root $\rho \in R$ of $X^2 - t_0 X + n_0$ and ring maps $t_1, \dots, t_a : \mathcal{O}_F \to R$ with $t_i(\omega) = \rho$. We require that every integer prime to $p$ is a unit in $R$. For $i \neq j$ the elements $t_i(x) - t_j(x)$ generate the unit ideal, and for every map $\beta : R \to k$ to a field of characteristic $p$ the kernels of $\beta t_i$ and $\beta t_j$ differ.

Lean: `GlobalTheory.UPel.HT.Base`.

**Definition 8.1.3 (Object of level $N$).** Let $b$ be a base over $R$, $N \geq 0$, and $s : S \to \operatorname{Spec} R$ a scheme over $R$. An *object of level $N$* over $s$ consists of an abelian scheme $A$ over $S$, an action of $O$ on $A$, and a line bundle $P$ on $A \times_S A$. We require that $P$ is trivial on $0 \times A$ and on $A \times 0$, symmetric, with $\Delta^* P$ relatively ample, that its kernel is killed by an integer prime to $p$, and that it satisfies the Rosati condition for $*$. There is a condition on the Lie algebra of $A$ through the maps $t_i$. Finally there is an $O$-linear map $\eta : \Lambda \to A(S)$ with $\eta(N\Lambda) = 0$ that, at every geometric point of $S$, comes from an isomorphism of Tate modules compatible with $E$ and the Weil pairing. A *map of objects* over a map $f : S' \to S$ is a map of abelian schemes that identifies the first abelian scheme with the pullback of the second along $f$, commutes with $O$, carries $P$ to $P$ up to isomorphism, and carries $\eta$ to $\eta$.

Lean: `GlobalTheory.UPel.HT.Obj` (also `GlobalTheory.UPel.HT.ObjMap`).

**Definition 8.1.4 (Representing family and model).** A *representing family* of level $N$ over $b$ is a scheme $X$, a map $s : X \to \operatorname{Spec} R$ and an object $u$ of level $N$ over $s$ with the following property. For every scheme $S$, every $s' : S \to \operatorname{Spec} R$ and every object $o$ over $s'$ there is a unique $f : S \to X$ with $s f = s'$ such that a map of objects $o \to u$ over $f$ exists. A *model* of level $N$ over $b$ is a representing family such that $s$ is quasi-projective and smooth of relative dimension $a(n - 1)$.

Lean: `GlobalTheory.UPel.HT.RepFam` (also `GlobalTheory.UPel.HT.Model`).

### The auxiliary Siegel problem

Let $\zeta_M = e^{2\pi i/M}$ and $B_M = \mathbb{Z}[\zeta_M, 1/M] \subset \mathbb{C}$. Let $\langle a, b \rangle = \sum_{j=1}^{h} (a_j b_{h+j} - a_{h+j} b_j)$ be the standard symplectic form on $\mathbb{Z}^{2h}$.

**Definition 8.1.5 (Symplectic level structure).** Let $A$ be an abelian scheme over $S$ with a line bundle $P$ on $A \times_S A$, and let $s_1 : S \to \operatorname{Spec} B_M$. A *symplectic level $M$ structure* is an additive map $\lambda : \mathbb{Z}^{2h} \to A(S)$ with $M\lambda = 0$ such that, at every geometric point $x$ of $S$ over a map $\beta : B_M \to k$, the map $\lambda_x$ induces an isomorphism $(\mathbb{Z}/M)^{2h} \cong A_x[M]$ and the Weil pairing of $\Delta^* P$ satisfies $e_M(\lambda_x(a), \lambda_x(b)) = \beta(\zeta_M)^{2\langle a, b \rangle}$. A *Siegel object* of genus $h$ and level $M$ over $s_1$ is an abelian scheme $A$ over $S$ with a line bundle $P$ on $A \times_S A$, trivial on $0 \times A$ and on $A \times 0$ and symmetric, and a symplectic level $M$ structure. Its kernel is *killed by $d$* if $\Delta^* P$ is relatively ample and $d$ kills every point of $A$ in the kernel of the polarization.

We say that the Siegel problem $(h, M, d)$ is *representable* if there are a quasi-projective scheme $X$ over $B_M$ on which $d$ is a unit and a Siegel object $u$ over $X$ with kernel killed by $d$, such that every Siegel object over a scheme $S$ on which $d$ is a unit, with kernel killed by $d$, is the pullback of $u$ along a unique map $S \to X$ over $B_M$. We say that $b$ has *representable auxiliary level $(N, h, M)$* if there are a scheme $X$, maps $s : X \to \operatorname{Spec} R$ with $s$ quasi-projective and $s_1 : X \to \operatorname{Spec} B_M$, an object $u$ of level $N$ over $s$ and a symplectic level $M$ structure on $u$ with respect to $s_1$, such that every object of level $N$ with a symplectic level $M$ structure over $(t, t_1)$ comes from a unique $f$ with $s f = t$ and $s_1 f = t_1$ through a map of objects that carries one level structure to the other.

Lean: `GlobalTheory.UPel.HT.SDRep` (also `GlobalTheory.UPel.HT.HasLevelStructureOfLevel`).

The following four results are proved later in this chapter, and we use them here.

1. [Theorem 8.7.5](/entry/siegel-kernel-bounded-representable-of-coprime/): if $h \geq 1$, $M \geq 3$ is odd, $d > 0$ and $\gcd(M, d) = 1$, then the Siegel problem $(h, M, d)$ is representable.
2. [Theorem 8.17.3](/entry/harris-taylor-auxiliary-symplectic-level-representable/): let $R$ be noetherian, $b$ a base over $R$, $N \geq 3$ prime to $p$, $M \geq 3$ odd and prime to $p$, and $e$ prime to $p$ and to $M$ with $E(\Lambda, -) \supseteq e \Lambda^\vee$ as in part 3 of the datum. Let $h = \lfloor \operatorname{rk} \Lambda / 2 \rfloor$. If the Siegel problem $(h, M, e)$ is representable, then $b$ has representable auxiliary level $(N, h, M)$.
3. [Theorem 8.18.5](/entry/exists-representing-family-of-auxiliary-representation/): under the same hypotheses on $R$, $b$, $N$, $M$ and $e$, if $b$ has representable auxiliary level $(N, h, M)$, then there is a representing family of level $N$ over $b$ whose map to $\operatorname{Spec} R$ is quasi-projective.
4. [Theorem 8.19.5](/entry/smooth-of-relative-dimension-rep-fam-of-is-qproj-over/): let $R$ be noetherian, $b$ a base over $R$ and $N \geq 3$ prime to $p$. Every representing family of level $N$ over $b$ whose map to $\operatorname{Spec} R$ is quasi-projective is smooth of relative dimension $a(n - 1)$.

**Lemma 8.1.6 (The rank of the lattice).** For every datum $D$ for $p$, the rank of $\Lambda$ over $\mathbb{Z}$ is at least $2$.

Lean: `GlobalTheory.UPel.HT.Datum.two_le_finrank_La`.

*Proof.* The rank is $mn[F : \mathbb{Q}]$, a product of positive integers, so it is at least $1$. Suppose it is $1$ and let $v$ be a basis of $\Lambda$. For $x = \alpha v$ and $y = \beta v$ we get $E(x, y) = \alpha\beta E(v, v) = 0$, since $E$ is alternating. So $x \mapsto E(x, -)$ is zero, which contradicts its injectivity on $\Lambda \neq 0$. $\square$

### The representing family and the model

**Theorem 8.1.7 (Quasi-projective representing family).** Let $p$ be a prime, $D$ a datum for $p$, $R$ a [[noetherian|0670T59HGE]] ring, $b$ a base for $D$ over $R$, and $N \geq 3$ an integer prime to $p$. Then there is a representing family of level $N$ over $b$ whose map to $\operatorname{Spec} R$ is quasi-projective.

Lean: `GlobalTheory.UPel.HT.exists_repFam_qproj` (also `GlobalTheory.T.exists_quasiProjective_harrisTaylor_family`).

*Proof.* Part 3 of the datum gives an integer $e$ prime to $p$ with $E(\Lambda, -) \supseteq e\Lambda^\vee$. We have $e > 0$, because $\gcd(0, p) = p \neq 1$. Choose a prime $M \geq p + e + 3$. Then $M \geq 3$, and $M \neq 2$, so $M$ is odd. The primes $M$ and $p$ are distinct, because $M > p$, so $\gcd(M, p) = 1$. Since $0 < e < M$, the prime $M$ does not divide $e$, so $\gcd(M, e) = 1$. Let $h = \lfloor \operatorname{rk} \Lambda / 2 \rfloor$. By the lemma on the rank of the lattice, $h \geq 1$. Result 1 above, applied to $(h, M, e)$, shows that the Siegel problem $(h, M, e)$ is representable. Result 2 then shows that $b$ has representable auxiliary level $(N, h, M)$, and result 3 gives a representing family of level $N$ over $b$ with quasi-projective map to $\operatorname{Spec} R$. $\square$

**Theorem 8.1.8 (Integral model).** Let $p$ be a prime, $D$ a datum for $p$, $R$ a noetherian ring, $b$ a base for $D$ over $R$, and $N \geq 3$ an integer prime to $p$. Then a model of level $N$ over $b$ exists.

Lean: `GlobalTheory.UPel.HT.model_nonempty`.

*Proof.* The [theorem on quasi-projective representing families](/entry/exists-rep-fam-qproj/) gives a representing family $(X, s, u)$ of level $N$ over $b$ with $s$ quasi-projective. Result 4 above shows that $s$ is smooth of relative dimension $a(n - 1)$. So $(X, s, u)$ is a model. $\square$

Only the properties $M \geq 3$, $M$ odd, $\gcd(M, p) = 1$ and $\gcd(M, e) = 1$ of the prime $M$ enter the proof. The auxiliary level $M$ need not be prime to $N$, since the level $N$ structure and the level $M$ structure are separate data.

**Remark 8.1.9 (Formalization).** The prime $M$ is chosen with the infinitude of primes and used only through these four properties: [ExistsQuasiProjectiveHarrisTaylorFamily.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsQuasiProjectiveHarrisTaylorFamily.lean#L24). The integer $h$ is the rank of $\Lambda$ divided by $2$ in the natural numbers, and the relative dimension $a(n - 1)$ uses subtraction of natural numbers, which is exact since $n \geq 1$: [NotCompactOfMEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NotCompactOfMEqOne.lean#L204). The universal property asks for a unique map $f$ and only for the existence of a map of objects over $f$, not for a unique one: [ToRepFam.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ToRepFam.lean#L16). A Siegel object does not record its relative dimension; it is $h$ at every geometric point by the isomorphism with $(\mathbb{Z}/M)^{2h}$. The wrapper [ExistsQuasiProjectiveHarrisTaylorFamilyStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsQuasiProjectiveHarrisTaylorFamilyStatement.lean#L6) raises the heartbeat limit. We summarized the datum and the objects; the trace condition, the Lie condition and the compatibility with the Weil pairing are spelled out in the definitions. We opened the statements of the four results used, not their proofs.
