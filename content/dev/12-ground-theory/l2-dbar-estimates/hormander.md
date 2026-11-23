---
id: hormander
title: Hörmander's L2 estimate on étale Stein spaces
kind: theorem
decl: ReciprocityTheory.L2DbarEstimates.hormander
module: ReciprocityTheory.L2DbarEstimates.NormFibrations.Hormander
covers: 395
status: drafted
drafted_by: writer@claude
---
This theorem proves `HStatement`, a weighted $L^2$ estimate for the $\bar\partial$ equation. It is one of the analytic inputs below the literature layer of the proof ([EveryCharacter from the literature and VWin](/step/every-character-of-literature/)). The declaration only passes proved statements along. The real content is in [the assembly `hStatement_of`](/entry/h-statement-of/).

## Statement

Let $X$ be an étale Stein space of dimension $n$: a space $M$ with a local homeomorphism $z : M \to \mathbb{C}^n$ and a smooth exhaustion with nonnegative Levi form (`EtaleStein`). Let $\varphi$ be smooth with nonnegative Levi form, $F_0$ smooth, and $h \ge 0$ measurable with
$$|\bar\partial F_0(x) \cdot \bar\xi|^2 \le h(x)\, \operatorname{Re} \mathcal{L}_\varphi(x)(\xi, \xi) \quad \text{for all } x \in M,\ \xi \in \mathbb{C}^n.$$

**Theorem** (`HStatement n M`). There is a holomorphic $F$ with
$$\int_M |F_0 - F|^2 e^{-\varphi}\, d\mathrm{vol} \le \int_M h\, e^{-\varphi}\, d\mathrm{vol},$$
where $\mathrm{vol}(A) = \int_{\mathbb{C}^n} \#(A \cap z^{-1}(y))\, dy$ (`vol`).

So $u = F_0 - F$ solves $\bar\partial u = \bar\partial F_0$ with an $L^2$ bound. This has the form of Hörmander's estimate (L. Hörmander, Acta Math. 113, 1965, 89 to 152).

## Proof

`hormander n M` is `F.hStatement_of n M` applied to eight proved statements: the twisted a priori inequality `E.ap`, integration by parts for $T^*$ (`E.tStarIbp`), the chain rule for the Levi form (`chain`), weak holomorphy is holomorphy (`C.reg`), and four facts on mollifiers (`B.moll_graph`, `B.moll_smooth`, `B.moll_support`, `B.kernel_std`).

## In the Lean code

The theorem is at [Hormander.lean](lean:ReciprocityTheory/L2DbarEstimates/NormFibrations/Hormander.lean#L24). `HStatement` is in [JacobianInterpolationStatement.lean](lean:ReciprocityTheory/L2DbarEstimates/JacobianInterpolationStatement.lean#L10). In the same file as the theorem, `skoda` applies it on $M \times \mathrm{Fin}\, p$ and `tw` applies it on $M$. `ot0` uses it through `tw`.
