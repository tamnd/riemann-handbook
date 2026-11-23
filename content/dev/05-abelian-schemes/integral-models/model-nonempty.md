---
id: model-nonempty
title: An integral model of a Harris-Taylor Shimura variety exists
kind: theorem
decl: GlobalTheory.UPel.HT.model_nonempty
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HarrisTaylorIntegralModelNonempty
covers: 2597
status: drafted
drafted_by: writer@claude
---
This theorem says that a PEL moduli problem of Harris-Taylor type has a smooth quasi-projective fine moduli scheme over any noetherian base in which the integers prime to $p$ are units. In the file of [the fixed points over an integral base](/entry/fixed-points-int-base-holds/), `ModelEx_holds` restates it as `ModelEx`. Its result goes into the [package of facts about the Kuga-Sato tower](/entry/kodaira-spencer-of-weight-one/) of the Galois row.

## Statement

Let $p$ be a prime. A *datum* $D$ for $p$ consists of:

- a CM field $F$ with complex conjugation $c \mapsto \bar c$, and $\omega \in \mathcal{O}_F$ with $\omega + \bar\omega = t$, $\omega\bar\omega = n_0$ in $\mathbb{Z}$, $t^2 - 4n_0 < 0$, $p \nmid t^2 - 4n_0$, and $X^2 - tX + n_0$ with a root mod $p$;
- an $\mathcal{O}_F$-order $O$, free of rank $m^2[F:\mathbb{Q}]$ over $\mathbb{Z}$ with $m \geq 1$, with an involution $*$ that is $c \mapsto \bar c$ on $\mathcal{O}_F$, and with $O \otimes \mathbb{Z}_p \cong M_m(\mathcal{O}_F \otimes \mathbb{Z}_p)$;
- an $O$-module $\Lambda$, free of rank $mn[F:\mathbb{Q}]$ with $n \geq 1$, with an alternating nondegenerate form $E$ for which $*$ is the adjoint, and an $e$ prime to $p$ with $e\Lambda^\vee \subseteq E(\Lambda)$;
- embeddings $\tau_1, \dots, \tau_a$ of $F$ that send $\omega$ to a root $\rho$ of $X^2 - tX + n_0$, and a complex structure $J$ on $\Lambda_\mathbb{R}$, positive for $E$ and commuting with $O$, with a trace condition.

A *base* $b$ over a ring $R$ is: integers prime to $p$ are units in $R$; a root $\rho \in R$ of $X^2 - tX + n_0$; maps $t_i \colon \mathcal{O}_F \to R$ with $t_i(\omega) = \rho$, pairwise comaximal and distinct mod $p$.

An *object* over $s \colon S \to \operatorname{Spec} R$ of level $N$ is an abelian scheme $A/S$ with an $O$-action and a line bundle $P$ on $A \times_S A$ (rigidified, symmetric, with $\Delta^*P$ relatively ample and kernel killed by an integer prime to $p$, and a Rosati condition for $*$), a condition on $\operatorname{Lie} A$ through the $t_i$, and an $O$-linear map $\eta \colon \Lambda \to A(S)$ with $\eta(N\Lambda) = 0$ that comes from an isomorphism of Tate modules compatible with $E$ at each geometric point.

A *model* of level $N$ is a scheme $X$ over $R$ with an object $u$ over $X$ such that $X$ is quasi-projective over $R$, smooth of relative dimension $a(n-1)$, and each object over $S$ is the pullback of $u$ along a unique $f \colon S \to X$.

**Theorem.** Let $R$ be noetherian and $b$ a base over $R$. If $N \geq 3$ and $\gcd(N, p) = 1$, then a model of level $N$ exists.

We have not checked this datum against Harris and Taylor (Annals of Math. Studies 151, 2001).

## Proof

1. [The existence of a quasi-projective representing family](/entry/exists-quasi-projective-harris-taylor-family/) gives $X$ and $u$ with the universal property, and $X$ quasi-projective over $R$.
2. `GlobalTheory.T.smoothOfRelativeDimension_repFam_of_isQProjOver` makes $X$ smooth of relative dimension $a(n-1)$. Its proof uses the infinitesimal lifting criterion (objects lift along square-zero thickenings of artinian rings) and the universal first-order tangent space.

## In the Lean code

The theorem is in [HarrisTaylorIntegralModelNonempty.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorIntegralModelNonempty.lean#L11). `Datum`, `Base`, `Obj` and `Model` are in [NotCompactOfMEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NotCompactOfMEqOne.lean#L13). The smoothness lemma is an alias of `RepFam.smoothOfRelativeDimension`. We have not opened its four lemmas, and we have not unfolded `LieMult` in the Lie condition.

The dimension `D.a * (D.n - 1)` uses natural subtraction, which is safe since `n_pos` gives $n \geq 1$. The universal property asks for a unique $f$ and only some isomorphism `ObjMap`, not a unique one.
